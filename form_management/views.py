from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import os

from userprofile.models import PointTransaction
from .models import *

@login_required
def index(request):
    return render(request, "form_management/index.html", {})

@csrf_exempt
@login_required
def form_response(request, form_id):

    form = Form.objects.get(pk = form_id)
    user_bought_list = PointTransaction.objects.filter(form_id = form, user_id = request.user, point__lt = 0)

    if request.user.username != form.owner.username:
        if not user_bought_list.exists():
            return HttpResponseRedirect(f"/form/{form_id}")

    if request.method == "POST":
        action = request.POST["action"]
        if action.lower() == "close-form":
            form.is_open = False
            form.save();
            return HttpResponseRedirect(reverse("form_response", args=(form_id,)))
        elif action.lower() == "sell-form":
            # User cannot sell their from if they are not close their form.
            if form.is_open:
                return HttpResponseRedirect(reverse("form_response", args=(form_id,)))
            
            response_count = FormResponse.objects.filter(form = form).count()
            # user cannot sell the zero response form.
            if response_count == 0:
                return HttpResponseRedirect(reverse("form_response", args=(form_id,)))

            points = Point.objects.filter(context = "SEL")
            selling_point = [point for point in points if point.lower_bound <= response_count <= point.upper_bound]
            selling_point = selling_point[0] if selling_point else 0 # make sure that the question number in the boundary, or not less than zero

            form.is_sale = True
            form.form_selling_point = selling_point
            form.save()
            return HttpResponseRedirect(reverse("form_response", args=(form_id,)))


    form_responses = FormResponse.objects.filter(form = form)
    questions = [section["question"] for section in form.design]
        

    return render(request, "form_management/form_response.html", {
        "form_name": form.form_name,
        "questions": questions, 
        "records": form_responses,
        "form": form,
    })

# =================================== APIs ===================================


@login_required
@csrf_exempt
def save_form(request):

    if request.method == "POST":
        data = json.loads(request.body)
        num_of_questions = len(data["design"])

        points = Point.objects.filter(context = "ANS")
        point = [point for point in points if point.lower_bound <= num_of_questions <= point.upper_bound][0]

        form = Form(
            form_name = data["formName"],
            description = data["description"],
            design = data["design"],
            owner = request.user,
            form_point = point,
            is_open = True,
        )
        form.save()


        return JsonResponse({"msg": "Save successfuly", "formId": form.id}, status = 201)
    
    return JsonResponse({"error": "POST request is required."}, status = 400)


@csrf_exempt
def upload_pic(request):
    if request.method == "POST": 

        image_update = request.FILES.get("img")
        form_id = request.POST.get("formId") # รับ formId ที่ส่งมาจาก JavaScript

        file_path = "static/form_management/imgs"
        
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        new_filename = f"{form_id}_formpic.jpg"  # ใช้ formId เป็นชื่อไฟล์
        file_location = os.path.join(file_path, new_filename)

        with open(file_location, 'wb') as destination:
            for chunk in image_update.chunks():
                destination.write(chunk)

        # Update the current file dir.
        form = Form.objects.get(pk = form_id)
        form.form_pic = file_location
        form.save()
    
    return JsonResponse({"msg": "success"})
    

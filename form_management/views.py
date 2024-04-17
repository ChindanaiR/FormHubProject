from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *

@login_required
def index(request):
    return render(request, "form_management/index.html", {})

@login_required
def form_response(request, form_id):

    form = Form.objects.get(pk = form_id)
    form_responses = FormResponse.objects.filter(form = form)
    print(form_responses[0].__dict__.keys())
    questions = [resp["question"] for resp in form_responses[0].response]
    print(form_responses)

    return render(request, "form_management/form_response.html", {
        "form_name": form.form_name,
        "questions": questions, 
        "records": form_responses,
        "is_open": form.is_open,
    })

@login_required
def my_forms(request):

    forms = Form.objects.filter(owner = request.user)
    
    return render(request, "form_management/myforms.html", {
        "title": "My Forms",
		"forms": forms
	})

# =================================== APIs ===================================


@login_required
@csrf_exempt
def save_form(request):

    if request.method == "POST":
        data = json.loads(request.body)
        num_of_questions = len(data["design"])
        print(num_of_questions)

        points = Point.objects.all()
        point = [point for point in points if point.lower_bound <= num_of_questions <= point.upper_bound][0]
        print(point.id)

        form = Form(
            form_name = data["formName"],
            description = data["description"],
            design = data["design"],
            owner = request.user,
            form_point = point,
            is_open = True,
        )
        form.save()
        return JsonResponse({"msg": "Save successfuly"}, status = 201)
    
    return JsonResponse({"error": "POST request is required."}, status = 400)

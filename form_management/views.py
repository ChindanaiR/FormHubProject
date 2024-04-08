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

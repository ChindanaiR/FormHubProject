from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *


def index(request):
    return render(request, "userprofile/index.html", {})


# API
def get_userinfo(request):  #ส่งข้อมูลไรบ้างไปยัง js
    
	if request.method == "GET":

		user = User.objects.get(pk = request.user.id)
		return JsonResponse({
			"name":user.username,
			"email":user.email,
		})
	

def update_userinfo(request):
	if request.method == "PUT":

		user = User.objects.get(pk = request.user.id)
		return JsonResponse({
			"name":user.username,
			"email":user.email
		})



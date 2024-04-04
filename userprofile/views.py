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
def get_userinfo(request):  #ส่งข้อมูลไรบ้างไปยัง js เพื่อโชว์หน้าเว็บ
    
	if request.method == "GET":

		user = User.objects.get(pk = request.user.id)
		return JsonResponse({
			"name":user.username,
			"email":user.email,
		})
	

	
@login_required
@csrf_exempt
def update_userinfo(request):
    if request.method == "PUT":
        # รับข้อมูลจาก request
        data = json.loads(request.body)
        new_username = data.get("username")
        new_email = data.get("email")

        # ตรวจสอบว่ามี username ซ้ำกันหรือไม่
        if new_username and User.objects.exclude(id=request.user.id).filter(username=new_username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        # ตรวจสอบว่ามี email ซ้ำกันหรือไม่ 
        if new_email and User.objects.exclude(id=request.user.id).filter(email=new_email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        # อัปเดตข้อมูล
        user = request.user
        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        user.save()

        return JsonResponse({'message': 'User info updated successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


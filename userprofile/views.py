from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import os

from .models import *


def index(request):
    user = User.objects.get(pk = request.user.id)

    # User's created forms
    user_forms = Form.objects.filter(owner = user)

    # Ranking
    responses = PointTransaction.objects.filter(user_id = user)
    num_responses = len(responses)

    if num_responses >= 50:
         rank = 'https://icons.iconarchive.com/icons/iconarchive/badge-trophy/256/Badge-Trophy-21-icon.png'
    elif num_responses >= 25:
         rank = 'https://icons.iconarchive.com/icons/iconarchive/badge-trophy/256/Badge-Trophy-Diamond-4-icon.png'
    else:
         rank = 'https://icons.iconarchive.com/icons/iconarchive/badge-trophy/256/Badge-Trophy-Rubin-2-icon.png'

    # Bought Datasets
    user_datasets = PointTransaction.objects.filter(user_id=user, point__lt = 0)

    return render(request, "userprofile/index.html", 
                  {"id":user.id,
                   "userpic":user.profile_img,
                   "user_forms":user_forms,
                   "rank": rank,
                   "user_datasets": user_datasets}
                   )


# API
def get_userinfo(request):  #ส่งข้อมูลไรบ้างไปยัง js เพื่อโชว์หน้าเว็บ
    
	if request.method == "GET":

		user = User.objects.get(pk = request.user.id)
		return JsonResponse({
            "id":user.id,
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



@csrf_exempt
def upload_pic(request):
    print("=" * 100)    
    if request.method == "POST": 

        image_update = request.FILES.get("img")
        print(image_update)
      

# ระบุตำแหน่งของไฟล์ที่ต้องการลบ
        file_path = f"{request.user.profile_img}" 
        print(file_path)
        
        if os.path.exists(file_path):
    # ลบไฟล์
            os.remove(file_path)
            print("ไฟล์ถูกลบแล้ว")
        else:
            print("ไม่พบไฟล์ที่ต้องการลบ")

        user = request.user
        new_filename = f"{request.user.id}_{request.user.username}.jpg"  # ชื่อไฟล์ใหม่ที่คุณต้องการ
        user.profile_img.save(new_filename, image_update)
        user.save()

        return JsonResponse({"img": str(request.user.profile_img)}, status = 200)
    
    return JsonResponse({"msg": "failed"})


def getpic(request):

    if request.method == "GET" and request:
        return JsonResponse({"img": str(request.user.profile_img)}, status = 200)

    return JsonResponse({"msg": "failed upload"})


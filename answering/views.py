from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.staticfiles import finders

import json

from .models import *


def index(request):

	if (request.user.is_authenticated):
		is_already_answered_form = FormResponse.objects.filter(responder = request.user).values("form_id").distinct()
		exclude_form_list = [item["form_id"] for item in is_already_answered_form]
		forms = Form.objects.filter(is_open = True).exclude(id__in=exclude_form_list)
	else:
		forms = Form.objects.filter(is_open = True)

	return render(request, "answering/index.html", {
		"title": "All Active Forms",
		"forms": forms,
	})

@login_required
def form_answering(request, form_id):
	return render(request, "answering/form.html", {})


# ================================= API =================================

@login_required
@csrf_exempt
@api_view(["GET"])
def get_form(request, form_id):
    
	if request.method == "GET":

		try:
			form = Form.objects.get(pk = form_id)

			# Ensure that the form owner cannot answer their form.
			if form.owner == request.user:
				return JsonResponse({"error": "You cannot answer your own form"}, status = 403)
			
			# Check if the form is close or not
			if not form.is_open:
				return JsonResponse({"error": "This form has been closed by the owner."}, status = 403)

			# Check if the user used to answer this form.
			response = FormResponse.objects.filter(responder = request.user, form = form)
			if response.exists():
				return JsonResponse({"error": "You have already answered this form."}, status = 403)
			


			print(form)
			return JsonResponse({
				"formName": form.form_name,
				"description": form.description,
				"design": form.design,
			}, status = 201)
		except:
			return JsonResponse({"error": "Invalid form."})

	return JsonResponse({"error": "Something went wrong"}, status = 400)


@login_required
@csrf_exempt
@api_view(["POST"])
def save_response(request):
	
	if request.method == "POST":

		data = request.data
		form = Form.objects.get(pk = data["formId"])

		# Check if the user has already answered the form
		response = FormResponse.objects.filter(responder = request.user, form = form)
		print(f"YEEEEEEEEEEEEEEEEEEEEE {response.exists()}")
		if response.exists():
			return JsonResponse({"error": "You have already answered this form."}, status = 403)
		
		# Save the response
		form_response = FormResponse(
			form = form,
			responder = request.user,
			response = data["response"],
		)
		form_response.save()

		# Record the point
		point_tracsaction = PointTransaction(
			point = form.form_point.point,
			form_id = form,
			user_id = request.user,
		)
		point_tracsaction.save()

		return JsonResponse({"msg": "Your response has been saved successfully."}, status = 200)
	
	return JsonResponse({"error": "Only POST request is allowed"}, status = 403)

# =======================================================================

@csrf_exempt
def get_form_image(request):
    # ตรวจสอบว่ามีรูปภาพตามที่ต้องการหรือไม่
	
	if request.method == "POST":
		json_data = request.body
		data = json.loads(json_data)
		form_id=data['form_id']


	image_path = f"answering/imgs/{form_id}_formpic.jpg"
	
	if finders.find(image_path):
		return JsonResponse({'image_path': f"/static/answering/imgs/{form_id}_formpic.jpg"})
	else:
		# หากไม่มีรูปภาพตามที่ต้องการใช้รูปภาพที่สร้างมาใหม่แทน
		return JsonResponse({'image_path': "/static/answering/imgs//no-pic.png"}) 
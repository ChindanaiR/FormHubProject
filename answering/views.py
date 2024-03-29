from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json

from .models import *


def index(request):

	forms = Form.objects.filter(is_open = True)

	return render(request, "answering/index.html", {
		"forms": forms
	})


def form_answering(request, form_id):
	return render(request, "answering/form.html", {})


# ================================= API =================================


# @login_required
# @csrf_exempt
def get_form(request, form_id):
    
	if request.method == "GET":

		form = Form.objects.get(pk = form_id)
		print(form)
		return JsonResponse({
			"formName": form.form_name,
			"description": form.description,
			"design": form.design,
		})

		# return JsonResponse({
		# 	"formName": "Trying a rendering logic",
		# 	"design": 	[
		# 					{
		# 						"section": 1,
		# 						"type": "checkbox",
		# 						"question": "Test checkbox",
		# 						"options": [
		# 							"234567",
		# 							"rtyuio",
		# 							"rtyui",
		# 							"bsdfsdf"
		# 						]
		# 					},
		# 					{
		# 						"section": 2,
		# 						"type": "dropdown",
		# 						"question": "Test dropdown",
		# 						"options": [
		# 							"12345",
		# 							"567890",
		# 							"dfghjkl",
		# 							"asdas"
		# 						]
		# 					},
		# 					{
		# 						"section": 3,
		# 						"type": "checkbox",
		# 						"question": "checkbox again",
		# 						"options": [
		# 							"23456",
		# 							"hjkl;",
		# 							"67890-"
		# 						]
		# 					},
		# 					{
		# 						"section": 4,
		# 						"type": "radio",
		# 						"question": "Test radio",
		# 						"options": [
		# 							"asdasd",
		# 							"adasd",
		# 							"45678",
		# 							"tyui"
		# 						]
		# 					},
		# 					{
		# 						"section": 5,
		# 						"type": "radio",
		# 						"question": "Test radio 2",
		# 						"options": [
		# 							"12345678",
		# 							"0987654",
		# 							"12345678",
		# 							"09876543"
		# 						]
		# 					},
		# 					{
		# 						"section": 6,
		# 						"type": "long",
		# 						"question": "Test long text",
		# 					},
		# 					{
		# 						"section": 7,
		# 						"type": "short",
		# 						"question": "Test short text",
		# 					},
		# 					{
		# 						"section": 8,
		# 						"type": "file",
		# 						"question": "Test file upload",
		# 					},
		# 					{
		# 						"section": 9,
		# 						"type": "date",
		# 						"question": "Test date",
		# 					},
		# 					{
		# 						"section": 10,
		# 						"type": "time",
		# 						"question": "Test time",
		# 					},
		# 				]
		# }, status = 201)
	return JsonResponse({"error": "Something went wrong"}, status = 400)
# =======================================================================
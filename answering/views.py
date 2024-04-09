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
import json

from .models import *


def index(request):

	forms = Form.objects.filter(is_open = True)

	return render(request, "answering/index.html", {
		"forms": forms
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

		form = Form.objects.get(pk = form_id)
		print(form)
		return JsonResponse({
			"formName": form.form_name,
			"description": form.description,
			"design": form.design,
		}, status = 201)

	return JsonResponse({"error": "Something went wrong"}, status = 400)


@login_required
@csrf_exempt
@api_view(["POST"])
def save_response(request):
	
	if request.method == "POST":
		data = request.data
		form_response = FormResponse(
			form = Form.objects.get(pk = data["formId"]),
			responder = request.user,
			response = data["response"],
		)
		form_response.save()

		return JsonResponse({"msg": "Response saved."}, status = 200)
	
	return JsonResponse({"error": "Only POST request is allowed"}, status = 403)

# =======================================================================
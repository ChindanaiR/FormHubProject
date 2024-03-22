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
    return render(request, "answering/index.html", {})


# ================================= API =================================
# @login_required
# @csrf_exempt
def get_form(request):
    
	if request.method == "GET":
		return JsonResponse({
			"formName": "Trying a rendering logic",
			"design": 	[
							{
								"section": 1,
								"type": "dropdown",
								"question": "This is dropdown question",
								"options": [
									"first",
									"second",
									"third!",
									"another one"
								]
							},
							{
								"section": 2,
								"type": "checkbox",
								"question": "Let's try the checkboxes question",
								"options": [
									"First choice",
									"The second",
									"This is the thied",
									"how about this",
									"do you want to try this",
									"yeeeeee"
								]
							}
						]
		}, status = 201)
	return JsonResponse({"error": "Something went wrong"}, status = 400)
# =======================================================================
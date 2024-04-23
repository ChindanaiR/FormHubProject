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
    return render(request, "authentication/index.html", {})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "authentication/login.html", {
                "message": "Invalid username or password."
            })
    else:
        # Check if the user is already authenticated
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def register(request):

    if request.method == "POST":

        # Get the value from register form
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        username = request.POST["acctname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Ensure password matches confirmation
        if password != confirmation:
            return render(request, "authentication/register.html", {
                "error": "Passwords must match.",
                "data": {
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                    "email": email,
                    "student_id": student_id,
                    "password": password,
                }
            })

        # Attempt to create new user
        try:
            if User.objects.filter(email = email).exists():
                return render(request, "authentication/register.html", {
                    "error": "Email is already taken.",
                    "data": {
                        "first_name": first_name,
                        "last_name": last_name,
                        "username": username,
                        "email": email,
                        "student_id": student_id,
                        "password": password,
                    }
                })

            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                student_id = student_id,
                password = password,
            )
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "authentication/register.html", {
                "error": "Username is already taken.",
                "data": {
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                    "email": email,
                    "student_id": student_id,
                    "password": password,
                }
            })
        
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        # check if the user is already authenticated
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request, "authentication/register.html")
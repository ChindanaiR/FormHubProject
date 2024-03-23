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
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "authentication/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        # check if the user is already authenticated
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "authentication/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "authentication/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        # check if the user is already authenticated
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request, "authentication/register.html")
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # API route
    path("api/get_form_data/", views.get_form, name="get_form"),
]
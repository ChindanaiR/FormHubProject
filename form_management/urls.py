from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # ----------------- API routes -----------------
    path("api/save_form", views.save_form, name="save"),
]
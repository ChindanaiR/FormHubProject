from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("responses", views.form_response, name="form_response"),

    # ----------------- API routes -----------------
    path("save_form/", views.save_form, name="save"),
]
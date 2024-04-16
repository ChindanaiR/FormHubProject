from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("my-forms", views.my_forms, name="my-forms"),
    path("responses/<int:form_id>", views.form_response, name="form_response"),

    # ----------------- API routes -----------------
    path("save_form/", views.save_form, name="save"),
]
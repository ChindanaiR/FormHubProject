from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("my-forms", views.my_forms, name="my_forms"),
    path("responses/<int:form_id>", views.form_response, name="form_response"),
    path("upload",views.upload_pic,name="upload"),

    # ----------------- API routes -----------------
    path("save_form/", views.save_form, name="save"),
]
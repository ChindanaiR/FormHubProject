from django.urls import path
from . import views

app_name = "answering"
urlpatterns = [
    path("", views.index, name="index"),
    path("form/<int:form_id>", views.form_answering, name="answering"),
    # API route
    path("get_form_data/<int:form_id>", views.get_form, name="get_form"),
    path("save_response/", views.save_response, name="save_resp"),
    path("get_form_image/", views.get_form_image, name="get_form_image"),
    path("dataset/", views.dataset, name="dataset")
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form/<int:form_id>", views.form_answering, name="answering"),
    # API route
    path("get_form_data/<int:form_id>", views.get_form, name="get_form"),
    path("save_response/", views.save_response, name="save_resp")
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("get_userinfo",views.get_userinfo,name="get_userinfo"),
    path("update_userinfo",views.update_userinfo,name="update_userinfo")
]
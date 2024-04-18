from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("redeem/<int:redeem_id>", views.redeem, name="redeem"),

    path("check_point/", views.check_point, name="check_point"),
    path("get_point/", views.get_point, name="get_point"),


]
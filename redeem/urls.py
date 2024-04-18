from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("redeem/<int:redeem_id>", views.redeem, name="redeem"),
    path("get_point/", views.get_point, name="get_point"),
    # path("dataset_page/", views.)

]
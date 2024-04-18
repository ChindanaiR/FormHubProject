from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_id>", views.profile, name="profile"),
    path("get_userinfo",views.get_userinfo,name="get_userinfo"),
    path("update_userinfo",views.update_userinfo,name="update_userinfo"),
    
    path("api/upload",views.upload_pic,name="upload_pic"),
    path("api/getpic",views.getpic,name="getpic")

]
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    student_id = models.CharField(max_length = 10, null = True)
    profile_img = models.ImageField(
        upload_to="static/userprofile/imgs", 
        null = True,
        default = "static/userprofile/imgs/default.jpg")

    def __str__(self):
        return f"{self.username}"
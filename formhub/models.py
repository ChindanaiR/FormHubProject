from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Test(models.Model):
    demo = models.CharField(max_length=225)


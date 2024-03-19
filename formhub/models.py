from django.db import models
from django.contrib.auth.models import AbstractUser

# just for demonstration of working with git in a team
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    prefix = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    th_first_name = models.CharField(max_length=255, null=True, blank=True)
    th_last_name = models.CharField(max_length=255, null=True, blank=True)
    line_id = models.CharField(max_length=255, null=True, blank=True)
    line_name = models.CharField(max_length=255, null=True, blank=True)  # In case searching name in LineOA
    birthdate = models.DateField(null=True, blank=True)


class Bank:
    KASIKORN = "kasikorn"
    SCB = "scb"
    BANGKOK = "bangkok"
    KRUNGSRI = "krunsri"
    KRUNGTHAI = "krungthai"
    TTB = "ttb"
    AOMSIN = "aomsin"

    BANK_CHOICE = [
        (KASIKORN, "Kasikorn"),
        (SCB, "SCB"),
        (BANGKOK, "Bangkok"),
        (KRUNGSRI, "Krungsri"),
        (KRUNGTHAI, "Krungthai"),
        (TTB, "TTB"),
        (AOMSIN, "Aomsin"),
    ]

    BANK_DICT = dict(BANK_CHOICE)


class Teacher(models.Model):
    """
    Class name: Teacher
    Class description: the Teacher class is for gathering infomation of teacher.
    This class extend from core.User class model
    """

    abstract_user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    id_card_number = models.CharField(max_length=255)
    info = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=1024, null=True, blank=True)
    is_active = models.BooleanField(max_length=255, default=True)
    bank_account_number = models.CharField(default=0, null=True, blank=True)
    bank_name = models.CharField(max_length=255, choices=Bank.BANK_CHOICE, default="", null=True, blank=True)
    bank_account_name = models.CharField(max_length=255, default="", null=True, blank=True)


    def __str__(self):
        return self.abstract_user.nickname + " (" + self.abstract_user.first_name + ")"
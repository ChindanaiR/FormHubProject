from django.db import models
from form_management.models import Form, FormResponse
from authentication.models import User

class PointTransaction(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    point = models.IntegerField()
    form_id = models.ForeignKey(Form, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return f"{self.point} ({self.form_id})"

class RedeemItem(models.Model):
    redeem_code = models.CharField(max_length=3) # DCT, PRZ, CSH, DST
    description = models.CharField(max_length=150) # details
    point = models.IntegerField() 

class RedeemTransaction(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    point = models.IntegerField()
    redeem = models.ForeignKey(RedeemItem, on_delete = models.CASCADE, null = True)
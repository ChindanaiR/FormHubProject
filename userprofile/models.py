from django.db import models
from form_management.models import Form
from authentication.models import User


class TransactionCode(models.Model):
    transaction_code = models.CharField(max_length = 3)
    description = models.CharField(max_length = 150)


class PointTransaction(models.Model):
    transaction_id = models.ForeignKey(TransactionCode, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    point = models.IntegerField()
    form_id = models.ForeignKey(Form, on_delete = models.CASCADE, null = True)

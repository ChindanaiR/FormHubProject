from django.db import models
from authentication.models import User
from form_management.models import Form


class FormResponse(models.Model):
    form_id = models.ForeignKey(Form, on_delete = models.CASCADE)
    responder = models.ForeignKey(User, on_delete = models.CASCADE)
    response = models.JSONField()
    answering_time = models.DateTimeField(auto_now_add = True)

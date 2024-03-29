from django.db import models
from authentication.models import User


class Point(models.Model):
    form_size = models.CharField(max_length = 2)
    point = models.IntegerField()
    description = models.CharField(max_length = 50, null = True)
    lower_bound = models.IntegerField()
    upper_bound = models.IntegerField()

    def __str__(self):
        return f"Form Size: {self.form_size} ({self.lower_bound} - {self.upper_bound})"


class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.category_name}"
    

class Form(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    form_name = models.CharField(max_length = 125)
    description = models.CharField(max_length = 450)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    design = models.JSONField()
    creation_timestamp = models.DateTimeField(auto_now_add = True)
    publish_timestamp = models.DateTimeField(null = True)
    is_open = models.BooleanField(default = False)
    is_sale = models.BooleanField(default = False)
    form_point = models.ForeignKey(Point, on_delete = models.CASCADE, related_name="form_point")

    def __str__(self):
        return f"{self.form_name} ({self.owner})"
    
    def serialize(self):
        return {
            'owner': self.owner.username,
            'form_name': self.form_name,
            'description': self.description,
            'category': self.category,
            'design': self.design,
        }

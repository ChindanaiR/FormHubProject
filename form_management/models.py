from django.db import models
from authentication.models import User

POINT_CONTEXT = (
    ("SEL", "Selling"),
    ("ANS", "Answering")
)

class Point(models.Model):
    form_size = models.CharField(max_length = 2)
    context = models.CharField(max_length = 3, null = True, blank = True, choices = POINT_CONTEXT) # SEL = Selling, ANS = answering
    point = models.IntegerField()
    description = models.CharField(max_length = 50, null = True, blank = True)
    lower_bound = models.IntegerField()
    upper_bound = models.IntegerField()

    def __str__(self):
        return f"{self.context}: {self.point} ({self.lower_bound} - {self.upper_bound} Questions)"


class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.category_name}"
    

class Form(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    form_name = models.CharField(max_length = 125)
    description = models.CharField(max_length = 1000)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    design = models.JSONField()
    creation_timestamp = models.DateTimeField(auto_now_add = True)
    publish_timestamp = models.DateTimeField(null = True)
    is_open = models.BooleanField(default = False)
    is_sale = models.BooleanField(default = False)
    form_point = models.ForeignKey(Point, on_delete = models.CASCADE, related_name="form_point")
    form_selling_point = models.ForeignKey(Point, on_delete = models.CASCADE, null = True, blank = True, related_name="form_selling_point")
    form_pic = models.ImageField(
        upload_to="static/form_management/imgs", 
        null = True,
        default = "static/form_management/imgs/no-pic.png")

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

class FormResponse(models.Model):
    form = models.ForeignKey(Form, on_delete = models.CASCADE)
    responder = models.ForeignKey(User, on_delete = models.CASCADE)
    response = models.JSONField()
    answering_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Response from {self.responder}"
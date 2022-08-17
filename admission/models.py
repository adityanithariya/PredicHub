from django.db import models
from django.contrib.auth.models import User

from .vars import State, Gender, Category1, Category2
from django.core.validators import MaxValueValidator, MinValueValidator

# Utility Functions
def studentProfilePath(instance, filename):
    return f"admssion/student/{instance.user.username}/{filename}"

# Models
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(upload_to=studentProfilePath)
    phone_number = models.BigIntegerField(
        validators=[
            MaxValueValidator(9999999999),
            MinValueValidator(1000000000)
        ]
    )
    state = models.CharField(max_length=2, choices=State)
    gender = models.CharField(max_length=1, choices=Gender)
    category1 = models.CharField(max_length=3, choices=Category1)
    category2 = models.CharField(max_length=3, choices=Category2)
    _12th = models.FloatField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    JEEScore = models.FloatField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"


from email.policy import default
from django.db import models
from django.contrib.auth.models import User

from .vars import State, Gender, Category1, Category2
from django.core.validators import MaxValueValidator, MinValueValidator

# Variables
State.insert(0, (None, "Select your State"))
Gender.insert(0, (None, "Select Gender"))
Category1.insert(0, (None, "Select Caste"))
Category2.insert(0, (None, "Select Category"))

# Utility Functions
def studentProfilePath(instance, filename):
    return f"admission/student/{instance.user.username}/{filename}"
def collegeProfilePath(instance, filename):
    return f"admission/college/{instance.user.username}/{filename}"

def collegeProfilePath(instance, filename):
    return f"admission/student/{instance.user.username}/{filename}"

# Models
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    profile_image = models.ImageField(upload_to=studentProfilePath, default=None)
    state = models.CharField(max_length=2, choices=State)
    gender = models.CharField(max_length=1, choices=Gender)
    category1 = models.CharField(max_length=3, choices=Category1, verbose_name="Caste")
    category2 = models.CharField(max_length=3, choices=Category2, verbose_name="Category")
    _12th = models.FloatField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
        verbose_name="12th Percentage"
    )
    JEEScore = models.FloatField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
        verbose_name="JEE Percentile",
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"


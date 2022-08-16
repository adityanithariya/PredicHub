from django.db import models
from django.contrib.auth.models import User
from .vars import State

# Models
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=20, choices=State)
    

from django.contrib import admin
from .models import College, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(College)
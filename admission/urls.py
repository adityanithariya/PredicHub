from django.urls import path
from .views import admPredicForm, home

urlpatterns = [
    path("prediction-form", admPredicForm, name="admPredicForm"),
    path("home/", home, name="admhome"),
]

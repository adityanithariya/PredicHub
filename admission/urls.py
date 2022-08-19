from django.urls import path
from .views import admPredicForm

urlpatterns = [
    path("prediction-form", admPredicForm, name="admPredicForm")
]

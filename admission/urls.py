from django.urls import path
from .views import admPredicForm, collegeRegistration

urlpatterns = [
    path("prediction-form/", admPredicForm, name="admPredicForm"),
    path("college/register/", collegeRegistration, name="collegeRegister")
]

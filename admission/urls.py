from django.urls import path
from .views import admPredicForm, home, register, signin, signup, result

urlpatterns = [
    path("prediction-form", admPredicForm, name="admPredicForm"),
    path("home/", home, name="admhome"),
    path("prediction-form/", admPredicForm, name="admPredicForm"),
    path("register/<slug:mode>", register, name="admRegister"),
    path("signup/", signup, name="sign-up"),
    path("signin/", signin, name="sign-in"),
    path("result/", result, name="result")
]

from django.urls import path
from .views import admPredicForm, home, register
from admission import views

urlpatterns = [
    path("prediction-form", admPredicForm, name="admPredicForm"),
    path("home/", home, name="admhome"),
    path("prediction-form/", admPredicForm, name="admPredicForm"),
    path("register/<slug:mode>", views.register, name="admRegister"),
    path("signup/",views.signup,name="sign-up"),
    path("signin/",views.signin,name="sign-in"),
]

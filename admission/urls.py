from django.urls import path
from admission import views
from .views import admPredicForm, register

urlpatterns = [
    path("prediction-form/", admPredicForm, name="admPredicForm"),
    path("register/<slug:mode>", views.register, name="admRegister"),
    path("signup/",views.signup,name="sign-up"),
    path("signin/",views.signin,name="sign-in"),
]

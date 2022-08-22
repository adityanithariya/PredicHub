from django.urls import path
from admission import views
from .views import admPredicForm, register

urlpatterns = [
    path("prediction-form/", admPredicForm, name="admPredicForm"),
    path("register/", views.register, name="admRegister"),
    path("signup/",views.signup,name="sign-up"),
    
]

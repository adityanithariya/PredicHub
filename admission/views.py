from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.


def admPredicForm(request):
    context = {

    }
    return render(request, "admission/admissionPredicForm.html", context=context)


def register(request, mode="sign-up"):
    if request.method == "GET":
        context = {
            "mode":mode+"-mode"
        }
        return render(request, "sign.html", context=context)

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        
        if len(User.objects.filter(email=email)) != 0:
            messages.error(request, "User already exists!")
            return redirect('admRegister', mode="sign-in")

        user = User.objects.create_user(username=email.split('@')[0],email=email, password=password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect('admRegister', mode="sign-in")

    else:
        return HttpResponse("404 - Not Found", status=[404])

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email.split('@')[0], password=password)
        if user != None:
            login(request, user)
            return redirect('index')

    else:
        return HttpResponse("404 - Not Found")

import email
from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login

# Create your views here.


def admPredicForm(request):
    context = {

    }
    return render(request, "admission/admissionPredicForm.html", context=context)


def register(request):
    context = {

    }
    return render(request, "sign.html", context=context)

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        femail = request.POST['femail']
        fpass = request.POST['fpass']
        
        user = User.objects.create_user(femail.split('@')[0], femail, fpass)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect('index')


    else:    
        return HttpResponse("404 - Not Found")

def signin(request):
    if request.method == "POST":
        email = request.POST['femail']
        Password = request.POST['fpass']
        
        user = authenticate(request, username=email.split('@')[0], fpass=Password)
        if user != None:
            login(request, user)
            return redirect('index')

    else:
        return HttpResponse("404 - Not Found")
        




from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentRegistration

from .models import Student

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Views
def admPredicForm(request):
    if request.method == "POST":
        try:
            instance = get_object_or_404(Student, user=request.user)
            print(instance)
            form = StudentRegistration(request.POST or None, instance=instance)
        except Exception as e:
            form = StudentRegistration(request.POST or None)
        
        if form.is_valid():
            form = form.save(commit=False)
            form.JEEScore = 0
            form.user = request.user
            form.save()
            print("form saved")
            form = StudentRegistration(request.POST)
            return redirect('result')
        else:
            print("form invalid")
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    
    context = {
        "form": form,
    }
    return render(request, "admission/admissionPredicForm.html", context=context)

def home(request):
    return render(request, "admission/home.html")

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

        messages.success(request, "Login to continue!")
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
            return redirect('admPredicForm')

    else:
        return HttpResponse("404 - Not Found")

def result(request):
    return render(request, "admission/result.html")
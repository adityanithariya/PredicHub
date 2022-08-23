from django.shortcuts import render, redirect, get_object_or_404
from .forms import CollegeRegistration, StudentRegistration
from .models import Student

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
        else:
            print("form invalid")
            form = StudentRegistration(request.POST)
    else:
        form = StudentRegistration()
    
    context = {
        "form": form,
    }
    return render(request, "admission/admissionPredicForm.html", context=context)

def collegeRegistration(request):
    if request.method == "POST":
        form = CollegeRegistration(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            form = CollegeRegistration(request.POST or None)
        else:
            form = CollegeRegistration(request.POST)
    else:
        form = CollegeRegistration()
    context = {
        "form": form,
    }
    return render(request, "admission/collegeRegistration.html", context=context)

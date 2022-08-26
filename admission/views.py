from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentRegistration
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
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    
    context = {
        "form": form,
    }
    return render(request, "admission/admissionPredicForm.html", context=context)

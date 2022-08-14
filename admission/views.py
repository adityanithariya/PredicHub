from django.shortcuts import render

# Create your views here.
def admPredicForm(request):
    context = {

    }
    return render(request, "admission/admissionPredicForm.html", context=context)

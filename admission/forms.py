from django.forms import ModelForm
from .models import Student

class StudentRegistration(ModelForm):
    class Meta:
        model = Student

        fields = [
            "state",
            "gender",
            "category1",
            "category2",
            "_12th",
            "JEEScore",
        ]
    def __init__(self, *args, **kwargs):
        super(StudentRegistration, self).__init__(*args, **kwargs)
        self.fields['JEEScore'].required = False

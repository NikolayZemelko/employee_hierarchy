from django.forms import ModelForm

from .models import Employee


class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = [
            "date_created",
        ]

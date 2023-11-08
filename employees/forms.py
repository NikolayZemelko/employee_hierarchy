from django.forms import ModelForm
from django.utils.translation import gettext as _
from .models import Employee


class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = [
            "date_created",
        ]
        labels = {
            "first_name":  _("name"),
            "last_name":  _("last name"),
            "job_title":  _("position"),
            "date_offered":  _("offer date"),
            "salary":  _("salary"),
            "supervisor":  _("supervisor"),
        }

        help_texts = {
            "first_name": _("Enter the employee's name"),
            "last_name": _("Enter the employee's last name"),
            "job_title": _("Specify the employee's position"),
            "date_offered": _("Indicate the date the employee was hired"),
            "salary": _("Set employee salary"),
            "supervisor": _("Assign a manager to the employee"),
        }

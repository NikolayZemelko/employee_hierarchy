from django.views.generic import ListView
from .models import Employee


class EmployeesView(ListView):
    queryset = Employee
    template_name = "employees/index.html"

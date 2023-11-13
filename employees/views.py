from django.views import generic
from .models import Employee
from .forms import CreateEmployeeForm


class EmployeesView(generic.ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = "employees/index.html"


class EmployeeCreateView(generic.CreateView):
    form_class = CreateEmployeeForm
    success_url = 'employees-index'
    template_name = "employees/create.html"

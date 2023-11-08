from django.views import generic
from .models import Employee
from .forms import CreateEmployeeForm


class EmployeesView(generic.ListView):
    queryset = Employee
    template_name = "employees/index.html"


class EmployeeCreateView(generic.CreateView):
    form_class = CreateEmployeeForm
    success_url = 'employees-index'
    template_name = "employees/create.html"
    extra_context = {}

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from .forms import CreateEmployeeForm
from .models import Employee


class EmployeesView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    model = Employee
    context_object_name = 'employees'
    template_name = "employees/index.html"


class EmployeeCreateView(LoginRequiredMixin,
                         SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    form_class = CreateEmployeeForm
    success_url = reverse_lazy('employees-index')
    template_name = "employees/create.html"
    success_message = _("Employee successfully Created")
    extra_context = {"Button": "Create"}

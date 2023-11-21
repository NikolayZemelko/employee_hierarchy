from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic
from django_filters.views import FilterView

from .forms import CreateEmployeeForm
from .models import Employee
from .filters import EmployeeFilter


class EmployeesView(EmployeeFilter, FilterView):

    model = Employee
    paginate_by = 20
    ordering = 'first_name'
    filterset_class = EmployeeFilter
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

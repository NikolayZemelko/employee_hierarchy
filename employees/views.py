from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic
from django_filters.views import FilterView

from .filters import EmployeeFilter
from .forms import CreateEmployeeForm
from .models import Employee


class EmployeesView(EmployeeFilter, FilterView):
    model = Employee
    paginate_by = 20
    ordering = 'first_name'
    filterset_class = EmployeeFilter
    context_object_name = 'employees'
    template_name = "employees/employees_index.html"


class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'


class EmployeeCreateView(LoginRequiredMixin,
                         SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    form_class = CreateEmployeeForm
    success_url = reverse_lazy('employees-index')
    template_name = "employees/employee_create.html"
    success_message = _("Employee successfully Created")
    extra_context = {"Button": "Create"}


class EmployeeUpdateView(LoginRequiredMixin,
                         UserPassesTestMixin,
                         SuccessMessageMixin,
                         generic.UpdateView
                         ):
    pass


class EmployeeDeleteView(LoginRequiredMixin,
                         UserPassesTestMixin,
                         SuccessMessageMixin,
                         generic.DeleteView
                         ):
    pass

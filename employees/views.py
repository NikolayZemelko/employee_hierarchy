from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic
from django_filters.views import FilterView

from .filters import EmployeeFilter
from .forms import CreateEmployeeForm
from .mixins import AuthRequiredMixin
from .models import Employee


class EmployeesView(EmployeeFilter, FilterView):
    model = Employee
    paginate_by = 20
    ordering = 'first_name'
    filterset_class = EmployeeFilter
    context_object_name = 'employees'
    template_name = "employees/employees_index.html"


class EmployeeDetailView(AuthRequiredMixin,
                         generic.DetailView):
    login_url = reverse_lazy('login')
    model = Employee
    template_name = 'employees/employee_detail.html'
    permission_denied_message = _("You need to log in")
    extra_context = {"Button": _("Upload")}


class EmployeeCreateView(AuthRequiredMixin,
                         SuccessMessageMixin,
                         generic.CreateView):
    login_url = reverse_lazy('login')
    form_class = CreateEmployeeForm
    success_url = reverse_lazy('employees-index')
    template_name = "form.html"
    success_message = _("Employee successfully created")
    permission_denied_message = _("You need to log in")
    extra_context = {"Button": _("Create")}


class EmployeeUpdateView(AuthRequiredMixin,
                         SuccessMessageMixin,
                         generic.UpdateView
                         ):
    login_url = reverse_lazy('login')
    form_class = CreateEmployeeForm
    model = Employee
    success_url = reverse_lazy('employees-index')
    template_name = 'form.html'
    success_message = _("Employee successfully updated")
    permission_denied_message = _("You need to log in")
    extra_context = {"Button": _("Update")}


class EmployeeDeleteView(AuthRequiredMixin,
                         SuccessMessageMixin,
                         generic.DeleteView
                         ):
    login_url = reverse_lazy('login')
    model = Employee
    success_url = reverse_lazy('employees-index')
    template_name = "employees/employee_delete.html"
    success_message = _("Employee successfully deleted")
    permission_denied_message = _("You need to log in")
    extra_context = {"Button": _("Delete")}

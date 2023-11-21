from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic
from django_filters.views import FilterView

from .forms import CreateEmployeeForm
from .models import Employee
from .filters import EmployeeFilter


class EmployeesView(FilterView, generic.ListView):

    model = Employee
    paginate_by = 20
    filterset_class = EmployeeFilter
    context_object_name = 'employees'
    template_name = "employees/index.html"

    def get_ordering(self):

        if self.request.user.is_authenticated:
            return self.request.GET.get('sort_by', 'first_name')
        else:
            return super().get_ordering()


class EmployeeCreateView(LoginRequiredMixin,
                         SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    form_class = CreateEmployeeForm
    success_url = reverse_lazy('employees-index')
    template_name = "employees/create.html"
    success_message = _("Employee successfully Created")
    extra_context = {"Button": "Create"}

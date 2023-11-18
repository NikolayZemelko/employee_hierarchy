from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from .forms import CreateEmployeeForm
from .models import Employee
from .filters import EmployeeFilter


class EmployeesView(EmployeeFilter, generic.ListView):
    paginate_by = 20
    context_object_name = 'employees'
    template_name = "employees/index.html"

    def get_queryset(self):

        if self.request.user.is_authenticated:

            sort_by = self.request.GET.get('sort_by', 'first_name')
            return Employee.objects.order_by(sort_by)
        else:
            return Employee.objects.all()


class EmployeeCreateView(LoginRequiredMixin,
                         SuccessMessageMixin, generic.CreateView):
    login_url = 'login'
    form_class = CreateEmployeeForm
    success_url = reverse_lazy('employees-index')
    template_name = "employees/create.html"
    success_message = _("Employee successfully Created")
    extra_context = {"Button": "Create"}

from django.views.generic import ListView


class EmployeesView(ListView):

    template_name = "employees/index.html"

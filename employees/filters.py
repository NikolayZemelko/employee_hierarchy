import django_filters as filters
from .models import Employee


class EmployeeFilter(filters.FilterSet):
    supervisor = filters.ModelChoiceFilter(
        queryset=Employee.objects.filter(job_title="SR"))

    class Meta:
        model = Employee
        exclude = ['date_created']

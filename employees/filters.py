import django_filters as filters
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, HTML
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from .models import Employee


class EmployeeFilter(filters.FilterSet):
    supervisor = filters.ModelChoiceFilter(
        queryset=Employee.objects.filter(
            Q(job_title="SR") | Q(job_title="MD"))
    )
    date_offered = filters.DateRangeFilter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.helper = FormHelper()
        self.form.helper.form_class = 'row g-1'
        self.form.helper.layout = Layout(
            Field('first_name'),
            Field('last_name'),
            Field('date_offered'),
            Field('job_title', ),
            Field('salary'),
            Field('supervisor'),
            FormActions(
                Submit('filter', _('Filter'), css_class="btn-primary"),
                HTML(f'<a class="btn btn-primary" '
                     f'href="{reverse_lazy("employees-index")}">'
                     f'{_("Clear")}</a>')
            )
        )

    class Meta:
        model = Employee
        exclude = ['date_created']

from django.urls import path
from views import EmployeesView


urlpatterns = [
    path('', EmployeesView.as_view(), name='employees-index')
]

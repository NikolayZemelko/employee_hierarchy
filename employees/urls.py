from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmployeesView.as_view(), name='employees-index'),
    path('create', views.EmployeeCreateView.as_view(), name='employee-create'),
]

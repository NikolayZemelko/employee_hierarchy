from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmployeesView.as_view(),
         name='employees-index'),
    path('create/', views.EmployeeCreateView.as_view(),
         name='employee-create'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(),
         name='employee-detail'),
    path('<int:pk>/update/', views.EmployeeUpdateView.as_view(),
         name='employee-update'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(),
         name='employee-delete'),
]

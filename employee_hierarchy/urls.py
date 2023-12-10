from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from .views import BaseView, SignUpView
from .views import EmployeesLoginView, EmployeesLogoutView, EmployeesViewSet


router = routers.DefaultRouter()
router.register(r'employees', EmployeesViewSet)

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', EmployeesLoginView.as_view(),
         name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', EmployeesLogoutView.as_view(),
         name='logout'),
    path('employees/', include('employees.urls')),
    path('api/', include(router.urls))
]

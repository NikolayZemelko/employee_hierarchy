from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import (BaseView, SignUpView,
                    LoginView, LogoutView, EmployeeViewSet)

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('login/', LoginView.as_view(),
         name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(),
         name='logout'),
    path('employees/', include('employees.urls'))
]

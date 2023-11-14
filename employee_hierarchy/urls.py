from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include
from django.urls import path, reverse_lazy

from .views import BaseView, SignUpView

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html',
                                     next_page=reverse_lazy('employees-index'),
                                     extra_context={"Button": "Login"}),
         name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')),
         name='logout'),
    path('employees/', include('employees.urls')),
]

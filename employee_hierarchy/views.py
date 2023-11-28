from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView


class EmployeesLoginView(SuccessMessageMixin, LoginView):
    next_page = reverse_lazy("employees-index")
    template_name = "login.html"
    success_message = _('Successfully login')
    extra_context = {"Button": "Login"}


class EmployeesLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy("employees-index")
    template_name = "login.html"
    extra_context = {"Button": "Logout"}


class BaseView(generic.TemplateView):
    template_name = "base.html"


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = _('Successfully sign up')
    extra_context = {"Button": "Sign up"}

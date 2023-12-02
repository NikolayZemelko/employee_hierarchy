from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from employees.models import CEOEmployee


class EmployeesLoginView(SuccessMessageMixin, LoginView):
    next_page = reverse_lazy("employees-index")
    template_name = "login.html"
    success_message = _('Successfully login')
    extra_context = {"Button": "Login"}


class EmployeesLogoutView(LogoutView):
    next_page = reverse_lazy("employees-index")
    extra_context = {"Button": "Logout"}

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO,
                             'You are successfully logged out')
        return response


class BaseView(generic.TemplateView):
    template_name = "base.html"

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if CEOEmployee.objects.exists():
            self.extra_context['has_ceo'] = True
        return response


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    success_message = _('Successfully sign up')
    extra_context = {"Button": "Sign up"}

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class AuthRequiredMixin(LoginRequiredMixin):

    permission_denied_message = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request,
                                 messages.ERROR,
                                 self.permission_denied_message)
        return super().dispatch(request, *args, **kwargs)

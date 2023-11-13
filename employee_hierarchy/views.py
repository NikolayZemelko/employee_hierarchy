from django.views import generic


class BaseView(generic.RedirectView):
    pattern_name = 'employees-index'

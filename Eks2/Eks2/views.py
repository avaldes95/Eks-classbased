from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return super().get(request, *args, **kwargs)


class PeoplePage(TemplateView):
    template_name = 'peeps.html'

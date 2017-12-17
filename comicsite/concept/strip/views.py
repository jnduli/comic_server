from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

from concept.models import Concept
from concept.strip.models import Strip

# Create your views here.

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class StripCreate(CreateView, SuccessMessageMixin):
    model = Strip
    fields = ['image']
    success_message = "Strip file successfully uploaded"

    def get_success_url(self):
        return reverse('concept:detail_concept', args=[self.kwargs['pk']])

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.concept = Concept.objects.get(pk=self.kwargs['pk'])
        return super(StripCreate, self).form_valid(form)

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class StripUpdate(UpdateView, SuccessMessageMixin):
    model = Strip
    fields = ['image']
    success_message = "Strip file successfully updated"

    def get_object(self, queryset=None):
        strip = Concept.objects.get(id=self.kwargs['pk']).strip
        return strip

    def get_success_url(self):
        return reverse('concept:detail_concept', args=[self.kwargs['pk']])


# Create your views here.

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin

from concept.models import Concept
from gimp.models import Gimp

# Create your views here.

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class GimpCreate(CreateView, SuccessMessageMixin):
    model = Gimp
    fields = ['file_gimp']
    success_message = "Gimp file successfully uploaded"

    def get_success_url(self):
        return reverse('concept:detail_concept', args=[self.kwargs['pk']])

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.concept = Concept.objects.get(pk=self.kwargs['pk'])
        return super(GimpCreate, self).form_valid(form)

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class GimpUpdate(UpdateView, SuccessMessageMixin):
    model = Gimp
    fields = ['file_gimp']
    success_message = "Gimp file successfully updated"

    def get_object(self, queryset=None):
        gimp = Concept.objects.get(id=self.kwargs['pk']).gimp
        return gimp

    def get_success_url(self):
        return reverse('concept:detail_concept', args=[self.kwargs['pk']])


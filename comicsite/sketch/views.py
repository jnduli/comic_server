from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Sketch

# Create your views here.
@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class SketchCreate(CreateView, SuccessMessageMixin):
    model = Sketch
    fields = ['image']
    success_message = "Sketch successfully created"

    def get_success_url(self):
        return reverse('concept:detail_concept', args=[self.kwargs['pk']])

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.concept = Concept.objects.get(pk=self.kwargs['pk'])
        return super(SketchCreate, self).form_valid(form)

# TODO: add sketch edit command


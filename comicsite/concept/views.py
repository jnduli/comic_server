from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Concept
from .forms import ConceptForm

# Create your views here.

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class ConceptCreate(SuccessMessageMixin, CreateView):
    model = Concept
    form_class = ConceptForm
    # success_url = '/comics/system/' 
    success_message = "Concept successfully created"

    def get_success_url(self):
        return reverse('comics:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ConceptCreate, self).form_valid(form)

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class ConceptList(ListView):
    model = Concept

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class ConceptDetail(DetailView):
    model = Concept

@method_decorator(login_required(login_url=reverse_lazy('auth:login')),name='dispatch')
class ConceptUpdate(SuccessMessageMixin, UpdateView):
    model = Concept
    # fields = ['title', 'description', 'characters_no', 'conversation', 'deleted']
    form_class = ConceptForm
    success_message = "Concept successfully updated"

    def get_object(self, queryset=None):
        con = Concept.objects.get(id=self.kwargs['pk'])
        return con

    def get_success_url(self):
        return reverse('concept:detail_concept', kwargs={'pk':self.object.id})

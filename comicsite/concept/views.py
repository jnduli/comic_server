from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
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

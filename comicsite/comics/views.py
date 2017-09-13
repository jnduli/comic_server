from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from .models import Sketch, Comic
from concept.models import Concept
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
@login_required(login_url=reverse_lazy('auth:login'))
def system_page(request):
    return render(request, 'comics/homepage.html')

def page_not_made(request):
    return render(request, 'comics/page_not_made.html')


@method_decorator(login_required(login_url="/comics/login"), name="dispatch")
class ComicCreate(CreateView, SuccessMessageMixin):
    model = Comic
    fields = ['work_files']
    success_message = "Comic successfully created"

    def get_success_url(self):
        return reverse('comics:detail_concept', args=[self.kwargs['pk']])

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.sketch= Sketch.objects.get(pk=self.kwargs['pk'])
        return super(SketchCreate, self).form_valid(form)

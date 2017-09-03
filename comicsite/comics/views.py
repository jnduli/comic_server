from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from .models import Concept, Sketch, Comic
from .forms import ConceptForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
@login_required(login_url="/comics/login")
def system_page(request):
    return render(request, 'comics/homepage.html')

def page_not_made(request):
    return render(request, 'comics/page_not_made.html')

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = User.objects.get(email=email)
        user_logged = authenticate(request, username=user.username, password=password)
        if user_logged is not None:
            login_user(request, user_logged)
            return redirect(reverse('comics:index'))
        else:
            error_message = "Could not log in"
            return render(request, 'comics/login.html', {'error_message':"Could not log in"})
    except User.DoesNotExist:
        return render(request, 'comics/login.html', {'error_message':"Email does not exist"})

def logout(request):
    logout_user(request)
    return redirect(reverse('comics:login'))

@method_decorator(login_required(login_url="/comics/login"),name='dispatch')
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

@method_decorator(login_required(login_url="/comics/login"), name="dispatch")
class ConceptList(ListView):
    model = Concept

@method_decorator(login_required(login_url="/comics/login"), name="dispatch")
class ConceptDetail(DetailView):
    model = Concept

@method_decorator(login_required(login_url="/comics/login"),name='dispatch')
class SketchCreate(CreateView, SuccessMessageMixin):
    model = Sketch
    fields = ['image']
    success_message = "Sketch successfully created"

    def get_success_url(self):
        return reverse('comics:detail_concept', args=[self.kwargs['pk']])

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.concept = Concept.objects.get(pk=self.kwargs['pk'])
        return super(SketchCreate, self).form_valid(form)

# TODO: add sketch edit command

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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from .models import Concept
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def system_page(request):
    if request.user.is_authenticated:
        return render(request, 'comics/homepage.html')
    else:
        return render(request, 'comics/login.html')

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

@login_required(login_url="/comics/login")
def add_concept(request):
    if request.method == 'POST':
        return
    else:
        return render(request, 'comics/add_concept.html')

@method_decorator(login_required(login_url="/comics/login"),name='dispatch')
class ConceptCreate(SuccessMessageMixin, CreateView):
    model = Concept
    fields = ['characters_no','comicstrips_no','environment','conversation']
    success_url = '/comics/system/' 
    success_message = "Concept successfully created"

    # def get_success_url(self):
        # return reverse('comics:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ConceptCreate, self).form_valid(form)

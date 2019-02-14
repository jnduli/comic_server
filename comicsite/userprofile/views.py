from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserForm

# Create your views here.

@method_decorator(login_required(login_url=reverse_lazy('auth:login')), name='dispatch')
class UserDetail(DetailView):
    template_name = "userprofile/user_details.html"
    model = User

@method_decorator(login_required(login_url=reverse_lazy('auth:login')), name='dispatch')
class UserUpdate(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "userprofile/user_form.html"
    success_message = "Congrats. Your user details have been updated"

    def get_success_url(self):
        return reverse('userprofile:details', kwargs={'pk': self.request.user.id})

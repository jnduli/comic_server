from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

# Create your views here.

@method_decorator(login_required(login_url=reverse_lazy('auth:login')), name='dispatch')
class UserDetail(DetailView):
    template_name = "userprofile/user_details.html"
    model = User

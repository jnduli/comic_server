from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User

# Create your views here.
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
            return render(request, 'authenticate/login.html', {'error_message':"Could not log in"})
    except User.DoesNotExist:
        return render(request, 'authenticate/login.html', {'error_message':"Email does not exist"})

def logout(request):
    logout_user(request)
    return redirect(reverse('authenticate:login'))

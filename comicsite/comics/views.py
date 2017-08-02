from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def system_page(request):
    if request.user.is_authenticated:
        print("Some werhe here")
        return render(request, 'comics/main.html')
    else:
        return render(request, 'comics/login.html')

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = User.objects.get(email=email)
        user_logged = authenticate(request, username=user.username, password=password)
        if user_logged is not None:
            print("Some random debug info")
            login_user(request, user_logged)
            return redirect(reverse('comics:index'))
        else:
            print("Here cold")
            error_message = "Could not log in"
            return render(request, 'comics/login.html', {'error_message':"Could not log in"})
    except User.DoesNotExist:
        return render(request, 'comics/login.html', {'error_message':"Email does not exist"})

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def system_page(request):
    return render(request, 'comics/login.html')

def login(request):
    username = User.objects.get(email=someemail).username
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        #do some error checks
        play
    return
    

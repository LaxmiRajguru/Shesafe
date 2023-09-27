from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import CustomUser, CustomUserManager

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            
            user = CustomUser.objects.create_user(name= name,phone_number= phone_number, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_username = form.cleaned_data['username']
            login_password = form.cleaned_data['password']
            user = authenticate(request, username=login_username, password=login_password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request, 'index.html')

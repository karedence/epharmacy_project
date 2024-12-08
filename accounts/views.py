from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
    
    

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect pharmacists to their dashboard
            if user.is_pharmacist:
                return redirect('pharmacist_dashboard')
            else:
                return redirect('home')  # Redirect patients or other users
        else:
            messages.error(request, "Invalid login credentials")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
    

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect pharmacists to their dashboard
            if user.is_patient:
                return redirect('search_history')
            else:
                return redirect('home')  # Redirect patients or other users
        else:
            messages.error(request, "Invalid login credentials")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
        
    
    
    
     

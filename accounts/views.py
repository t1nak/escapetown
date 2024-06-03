from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
 
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserCreationForm
from .forms import UserProfileForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.contenttypes.models import ContentType


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

def login_view(request):

    #prevents access by logged in users
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'accounts/login.html', {
                'message': 'Invalid username and/or password'
            })
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:index')
        else:
            message = 'Please correct the error below.'
            return render(request, 'accounts/register.html', {
                'form': form,
                'message': message
            })
    else:
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})


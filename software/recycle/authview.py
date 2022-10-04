
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .form import CustomUserForm
from datetime import datetime, timezone

from django.conf import settings
from django.http import HttpResponseRedirect


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'registered successfully! login to continue')
            return redirect('/login/')
    context = {'form': form}
    return render(request, 'account/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username', None)
            passwd = request.POST.get('passwd', None)
            if name is not None and passwd is not None:
                user = authenticate(request, username=name, password=passwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in sucessfully')
                    return redirect("/")
                else:
                    messages.error(request, 'Invalid username or password')
                    return redirect('/login/')
        return render(request, 'account/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
    return redirect('/')

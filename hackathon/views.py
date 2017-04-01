# Django Imports
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponse
from django.urls import reverse

from .forms import *

"""
First thing anyone sees when the log into the site.
"""
def indexView(request):
    return render(request, 'index.html', {})

"""
Answers any general problems people hav with the service.
"""
def FAQView(request):
    return render(request, 'faq.html', {})

"""
Handles the activation of the user's key.
"""
def activationView(request, key):
    return render(request, '', {})

"""
Sends a new activation link to the user signing up for the service.
"""
def new_activation_link(request):
    return render(request, '', {})

"""
Handles the signup form for the users
"""
def signupView(request):
    return render(request,'',{})

"""
Manages the logging in of a user via django.auth functions.
"""
def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('logbook:index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'loginForm':form})

"""
Handles logging out of a user.
"""
def logoutView(request):
    return render(request, 'logout.html', {})

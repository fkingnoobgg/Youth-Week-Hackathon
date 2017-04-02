# Django Imports
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponse
from django.utils.crypto import get_random_string
from django.urls import reverse
import hashlib

from .forms import *

"""
First thing anyone sees when the log into the site.
"""
def indexView(request):
    services = Node.objects.all()
    return render(request, 'index.html', {'services':services})

"""
Answers any general problems people hav with the service.
"""
def FAQView(request):
    return render(request, 'faq.html', {})

"""
Handles the activation of the user's key.
"""
def activationView(request, key):
    return render(request, 'activation.html', {})

@login_required
def createHotSpotView(request):
    if request.method == "POST":
        NodeForm = AddMarkerForm(request.POST)
        if NodeForm.is_valid():
            htspt = HotSpot()
            htspt.node = NodeForm.cleaned_data['node']
            htspt.save()

            NodeForm.save()
    else:
        NodeForm = AddMarkerForm()
        return render(request, '', {'hotspot_form':NodeForm})

"""
Used for handling the voting system
"""
@login_required
def voteView(request):
    if request.is_ajax():
        if request.method == "POST":
            print(request.POST)
            if request.POST['action'] == 'up':
                print('UP')
            return redirect('hackathon:index')
    else:
        return HttpResponseForbidden()


"""
Used for creating a service for the map
"""
@login_required
def createServiceView(request):
    if request.method == "POST":
        NodeForm = AddMarkerForm(request.POST)
        if NodeForm.is_valid():
            srvc = Service()
            srvc.node = NodeForm.cleaned_data['node']
            srvc.save()

            NodeForm.save()
    else:
        NodeForm = AddMarkerForm()
        return render(request, '', {'hotspot_form':NodeForm})
        

"""
Sends a new activation link to the user signing up for the service.
"""
def new_activation_link(request):
    return render(request, '', {})

"""
Function to safely generate an activation key allowing the user verify their account.
"""
def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()

"""
Sign-up view creates a user from the entered SignUpForm and then sends the user
an email using a generated key to ensure the user has secure access to the said
email account.
"""
def signupView(request):
    if request.user.is_authenticated():
        return redirect('hackathon:index')
    '''
    View for handling student registration
    '''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = {}
            data['username'] = form.cleaned_data['username']
            data['email'] = form.cleaned_data['email']
            data['password'] = form.cleaned_data['password']
            data['activation_key'] = generate_activation_key(data['username'])
            
            data['email_path']="email_templates/ActivationEmail.txt"
            data['email_subject']="Activate your account"

            form.sendVerifyEmail(data)
            form.save(data)

            request.session['registered']=True #For display purposes
            return redirect('hackathon:login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'signupForm':form})

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
                return redirect('hackathon:index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'loginForm':form})

"""
Handles ending of a user's session.
"""
@login_required
def logoutView(request):
    logout(request)
    return redirect('hackathon:login')

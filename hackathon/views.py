from django.shortcuts import render

def indexView(request):
    return render(request, 'index.html', {})

def FAQView(request):
    return render(request, 'faq.html', {})

def activationView(request, key):
    return render(request, '', {})

def new_activation_link(request):
    return render(request, '', {})

def signupView(request):
    return render(request,'',{})

def loginView(request):
    return render(request, 'login.html', {})

def logoutView(request):
    return render(request, 'logout.html', {})

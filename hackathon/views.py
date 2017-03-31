from django.shortcuts import render

def indexView(request):
    return render(request, 'index.html', {})

def FAQView(request):
    return render(request, 'faq.html', {})

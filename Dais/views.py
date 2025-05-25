from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Dais/index.html')


def login(request):
    return render(request, 'Dais/login.html')

def modal(request):
    return render(request, 'Dais/modal.html')

def flexbox(request):
    return render(request, 'Dais/flexing.html')

def d_gray(request):
    return render(request, 'Dais/d_gray.html')

def acme_robots(request):
    return render(request, 'Dais/acme-robots.html')
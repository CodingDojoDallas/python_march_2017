from django.shortcuts import render


# CONTROLLER


# Create your views here.

def index(request):
    print "*"*50
    return render(request, 'first_app/index.html')

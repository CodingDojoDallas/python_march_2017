from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email

def index(request):
    return render(request, 'main_app/index.html')

def add(request):
    if request.method == 'POST':
        print request.POST
        if Email.objects.validate(request.POST['email']):
            Email.objects.create(address=request.POST['email'])
            messages.success(request, 'The email address you entered ({}) is a VALID email address. Thank you.'.format(request.POST['email']))
            return redirect('/success')
        else:
            messages.error(request, 'Please enter a valid email.')
    return redirect('/')

def success(request):
    context = {
        'emails': Email.objects.all()
    }
    print context
    return render(request, 'main_app/success.html', context)

def remove(request, id):
    if request.method == 'POST':
        Email.objects.get(id=id).delete()
        messages.success(request, 'The email has been successfully removed.')
    return redirect('/')

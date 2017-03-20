from django.shortcuts import render, redirect
from .models import User

# request.session:
    # messages: any errors or feedback to users
    # logged_in: true or false
    # user: first name of logged in user


def index(request):                                 # GET : RENDER
    context = request.session
    return render(request, 'index.html', context)

def register(request):                              # POST : REDIRECT
    results = User.objects.register(request.POST)
    if results[0] == False:
        request.session['messages'] = results[1]
        return redirect('/')
    elif results[0] == True:
        request.session['logged_in'] = True
        request.session['user'] = results[1]
        return redirect('/success')
    else:
        request.session['messages'] = "something went wrong"
        return redirect('/')

def login(request):                                 # POST : REDIRECT
    results = User.objects.login(request.POST)
    if results[0] == False:
        request.session['messages'] = results[1]
        return redirect('/')
    elif results[0] == True:
        request.session['logged_in'] = True
        request.session['user'] = results[1]
        return redirect('/success')
    else:
        request.session['messages'] = "something went wrong"
        return redirect('/')

def success(request):                               # GET : RENDER
    return render(request, 'success.html')

def logout(request):                                # POST : REDIRECT
    request.session.pop('user')
    if 'messages' in request.session:
        request.session.pop('messages')
    request.session['logged_in'] = False
    return redirect('/')

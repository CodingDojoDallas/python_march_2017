from django.shortcuts import render, redirect
from .models import User, Secret  # in theory, this is not needed here if all model interaction is done in models; try removing

# session is part of the request...

# TO DO: ADD if request.method == 'POST': to post methods


def index(request):                                 # GET : RENDER
    context = request.session
    return render(request, 'dojo_secrets/index.html', context)

def register(request):                              # POST : REDIRECT
    if request.method == 'POST':
        results = User.objects.register(request.POST)   # change parameter to request
        if results[0] == False:
            request.session['messages'] = results[1]
            return redirect('/')
        elif results[0] == True:
            print 'the results are', results
            request.session['logged_in'] = True
            print 'the id from the result is', results[1]
            request.session['id'] = results[1]
            request.session['first_name'] = results[2]
            request.session['most_popular'] = False
            return redirect('/secrets')
        else:
            request.session['messages'] = "something went wrong"
            return redirect('/')

def login(request):                                 # POST : REDIRECT
    if request.method == 'POST':
        results = User.objects.login(request.POST)   # change parameter to request
        if results[0] == False:
            request.session['messages'] = results[1]
            return redirect('/')
        elif results[0] == True:
            request.session['logged_in'] = True
            print 'the id from the result is', results[1]
            request.session['id'] = results[1]
            request.session['first_name'] = results[2]
            request.session['most_popular'] = False
            return redirect('/secrets')
        else:
            request.session['messages'] = "something went wrong"
            return redirect('/')

def logout(request):                                # POST : REDIRECT
    if 'messages' in request.session:
        request.session.pop('messages')
    request.session.pop('id')
    request.session.pop('first_name')
    request.session['logged_in'] = False
    return redirect('/')

def secrets(request):                               # GET : RENDER
    if not request.session['most_popular']:
        results = Secret.objects.secrets_recent()
        print 'the recent secret results are', results[1]
    else:
        results = Secret.objects.secrets_popular()
    context = { 'secrets': results[1] }
    print 'the secrets.html context is ', context
    return render(request, 'dojo_secrets/secrets.html', context)

def create(request):                                # POST : REDIRECT
    if request.method == 'POST':   # good practice!
        results = Secret.objects.create_secret(request)    # request.POST, request.session['id'])
    return redirect('/secrets')

def like(request, id):                                  # POST : REDIRECT
    if request.method == 'POST':   # good practice!
        results = Secret.objects.create_like(request, id)
    return redirect('/secrets')

def update(request):                                # POST : REDIRECT
    return redirect('/secrets')

def destroy(request):                               # POST : REDIRECT
    return redirect('/secrets')

def most_popular(request):
    if request.method == 'POST':
        request.session['most_popular'] = True
    return redirect('/secrets')

def form_and_recent(request):
    if request.method == 'POST':
        request.session['most_popular'] = False
    return redirect('/secrets')

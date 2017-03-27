from django.shortcuts import render, redirect
from .models import User, Secret
from django.contrib import messages


def index(request):                                 # GET : RENDER
    context = request.session
    print 'this is the request.session', request.session
    print 'this is the context', context
    print 'these are the messages', messages
    return render(request, 'dojo_secrets/index.html')

def register(request):                              # POST : REDIRECT
    if request.method == 'POST':
        results = User.objects.register(request.POST)   # change parameter to request
        if results[0] == False:
            request.session['session_messages'] = results[1]
            print '**********'
            print "results[1]", results[1]
            print '**********'
            print "request.session['session_messages']", request.session['session_messages']
            print '**********'
            for each in results[1]:
                messages.info(request, each)
            print 'these are the messages', messages
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
            request.session['session_messages'] = "something went wrong"
            return redirect('/')

def login(request):                                 # POST : REDIRECT
    if request.method == 'POST':
        results = User.objects.login(request.POST)   # change parameter to request
        if results[0] == False:
            request.session['session_messages'] = results[1]
            return redirect('/')
        elif results[0] == True:
            request.session['logged_in'] = True
            print 'the id from the result is', results[1]
            request.session['id'] = results[1]
            request.session['first_name'] = results[2]
            request.session['most_popular'] = False
            return redirect('/secrets')
        else:
            request.session['session_messages'] = "something went wrong"
            return redirect('/')

def logout(request):                                # POST : REDIRECT
    if 'session_messages' in request.session:
        request.session.pop('session_messages')
    request.session.pop('id')
    request.session.pop('first_name')
    request.session['logged_in'] = False
    return redirect('/')

#array of ids
def secrets(request):                               # GET : RENDER
    if not request.session['most_popular']:
        results = Secret.objects.secrets_recent(request)
    else:
        results = Secret.objects.secrets_popular()
    likes = User.objects.get_likes(request)
    # user.get_likes()
    # User.objects.get_likes()
    context = { 'secrets': results[1],
                'this_users_likes': likes[1]
              }
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

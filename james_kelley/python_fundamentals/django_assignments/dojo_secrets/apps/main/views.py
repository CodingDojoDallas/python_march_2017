from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import datetime
from django.utils import timezone
from django.db.models import Count

def index(request):
	return render (request, 'main/index.html')

def create_user(request):
	if User.objects.validate_user(request.POST):
		user = User.objects.create(
			first_name= request.POST.get('first_name'), 
			last_name= request.POST.get('last_name'),
			email= request.POST.get('email'),
			password= bcrypt.hashpw(request.POST.get('pass').encode(), bcrypt.gensalt()),
		)
		request.session['user_id'] = user.id
		return redirect('/secrets') 
	return redirect('/')

def login_user(request):
	if request.method == 'POST':
		login = User.objects.login_user(request.POST)
		if login:
			request.session['user_id'] = login[1].id
			return redirect('/secrets')
		else:
			messages.error(request, '*Invalid Credentials')
	return redirect('/')

def secrets(request):
	context = {
		'current_user' : User.objects.get(id=request.session['user_id']),
		'recent_secrets' : Secret.objects.annotate(num_likes = Count('likes')).all().order_by('-id')[:5],
		'elapsed_time' : datetime.datetime.now(),
	}
	return render (request, 'main/secrets.html', context)

def create_secrets(request):
	if request.method == 'POST':
		
		Secret.objects.create(
			secret = request.POST.get('secret'),
			creator = User.objects.get(id=request.session['user_id']),
			)
	return redirect ('/secrets')

def likes(request, id):
	person = User.objects.get(id=request.session['user_id'])
	secret = Secret.objects.get(id=id)
	secret.likes.add(person)

	return redirect ('/secrets')

def delete(request, id):
	Secret.objects.filter(id=id).delete()
	return redirect('/secrets')

def popular(request):
	context = {
		'popular_secrets' : Secret.objects.annotate(num_likes = Count('likes')).all().order_by('-likes'),
		'elapsed_time' : datetime.datetime.now() ,
	}
	return render (request, 'main/popular.html', context)






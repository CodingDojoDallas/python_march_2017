from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
from ..courses.models import Course

# def index(request):
# 	if not 'logged_in' in request.session or request.session['logged_in'] == False:
# 		return redirect('user_signin')
# 	return render(request, 'login_registration/index.html')

def index(request):
	return render(request, 'login_registration/index.html')

def create(request):
	result = User.objects.register(request.POST)
	if result[0] == False:
		for error in result[1]:
			messages.error(request, error['message'], extra_tags = error['tag'])
		return redirect('user_signin')
	else:
		request.session['logged_in'] = result[3]
		request.session['username'] = result[2]
		messages.success(request, result[1])
		return redirect('course_index')

def login(request):
	result = User.objects.login(request.POST)
	if result[0] == False:
		messages.error(request, result[1]['message'], extra_tags=result[1]['tag'])
		return redirect('user_signin')
	else:
		request.session['logged_in'] = result[3]
		request.session['username'] = result[2]
		messages.success(request, result[1])
		return redirect('course_index')

def logout(request):
	request.session.pop('logged_in')
	request.session.pop('username')
	return redirect('/')

def show(request, id):
	user = User.objects.get(id=id)
	courses_created = user.courses_created.all()
	courses_joined = user.courses_joined.all()
	other_courses = Course.objects.all().exclude(creator = id).exclude(students = user)
	context = {
		'user':user,
		'courses_created':courses_created,
		'courses_joined':courses_joined,
		'other_courses':other_courses
	}
	return render(request, 'login_registration/show.html', context)












from django.shortcuts import render, redirect
from models import Course, User

def index(request):
	if not 'logged_in' in request.session:
		return redirect('user_signin')
	courses = Course.objects.all()
	context = {'courses': courses}
	return render(request, 'courses/index.html', context)

def create(request):
	try:
		user = User.objects.get(id=request.session['logged_in'])
	except Exception, e:
		print e
	Course.objects.create(creator=user, name=request.POST['name'], description=request.POST['description'])
	return redirect('course_index')

def destroy(request, id):
	course = Course.objects.get(id=id)
	context = {'course': course}
	return render(request, 'courses/destroy.html', context)

def edit(request, id):
	course = Course.objects.get(id=id)
	context = {'course': course}
	return render(request, 'courses/edit.html', context)

def update(request, id):
	course = Course.objects.get(id=id)
	course.name = request.POST['name']
	course.description = request.POST['description']
	course.save()
	return redirect('course_index')

def delete(request, id):
	Course.objects.get(id=id).delete()
	return redirect('course_index')

def join(request, id):
	course = Course.objects.get(id=id)
	print course.__dict__
	student = User.objects.get(id=request.session['logged_in'])
	print student.__dict__
	course.students.add(student)
	course.save()
	print course.__dict__
	return redirect('course_index')
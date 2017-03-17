from django.shortcuts import render, redirect
from models import Course

def index(request):
	courses = Course.objects.all()
	context = {'courses': courses}
	return render(request, 'courses/index.html', context)

def create(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def destroy(request, id):
	course = Course.objects.get(id=id)
	context = {'course': course}
	return render(request, 'courses/destroy.html', context)

def edit(request, id):
	course = Course.objects.get(id=id)
	print course.__dict__
	context = {'course': course}
	return render(request, 'courses/edit.html', context)

def update(request, id):
	course = Course.objects.get(id=id)
	course.name = request.POST['name']
	course.description = request.POST['description']
	course.save()
	return redirect('/')

def delete(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')
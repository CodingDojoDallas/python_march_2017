from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Course

def index(request):
    context = {
        'course_list': Course.objects.all()
    }
    print context
    return render(request, 'main_app/index.html', context)

def add(request):
    if request.method == 'POST':
        print request.POST
        if not request.POST['name']:
            messages.error(request, 'Please enter a valid course name.')
            return redirect('/')
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        print 'Course added to database'
        messages.success(request, 'The course has been successfully added.')
    return redirect('/')

def destroy(request, id):
    if request.method == 'POST':
        context = {
    		'course': Course.objects.get(id=id)
    	}
        print context
        messages.error(request, 'WARNING: Deleted courses cannot be undone.')
        return render(request, 'main_app/destroy.html', context)
    return redirect('/')

def destroy_confirm(request, id):
    if request.method == 'POST':
        if request.POST['action'] == 'No':
            return redirect('/')
        else:
            Course.objects.get(id=id).delete()
            messages.success(request, 'The course has been successfully removed.')
    return redirect('/')

from django.shortcuts import render, redirect
from .models import Course

# url                     METHOD                          METHOD DIRECTION
# /                       def index (show form and data)  render template index.html
# #/courses/add/validate  def validate                    redirect(/add)
# /courses/add            def add (add to db)             redirect(/)
# /courses/destroy/<id>   def destroy                     render template destroy.html
# /courses/delete/<id>    def delete                      redirect(/)

def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, 'index.html', context)

# ADD VALIDATION - here, or in models?...
# def useradd(request):
#     return redirect('/add')

def add(request):
    name = request.POST['name']
    description = request.POST['description']
    Course.objects.create(name=name, description=description)
    return redirect('/')


def destroy(request, id):
    course = Course.objects.get(id=id)
    context = {'course':course}
    return render(request, 'destroy.html', context)

def delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')

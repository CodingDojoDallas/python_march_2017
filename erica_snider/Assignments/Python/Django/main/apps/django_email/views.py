from django.shortcuts import render, redirect
from .models import Email

# Create your views here.
def index(request):
    if 'message' not in request.session:
        request.session['message'] = "null"

    context = { 'message': request.session['message'] }

    return render(request, 'index.html', context)

def validate(request):
    email = request.POST['email']
    validation = Email.objects.validate(email)

    print (type(email))

    if 'errors' in validation:
        request.session['message'] = validation['errors'][0] #'Email is not valid!' ## validation.errors
        return redirect('/')
    elif 'success' in validation:
        Email.objects.create(email=email)
        return redirect('/success')
    else:
        return alert('error!')

def success(request):
    emails = Email.objects.all()
    context = {'emails':emails}
    print context
    return render(request, 'success.html', context)

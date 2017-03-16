from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def index(request):
    # Initialize session counter if one doesn't exist
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'main_app/index.html')

def result(request):
    print request.POST
    if request.method == 'POST':
        # Deny the submission if the user did not enter a name
        if not request.POST['name']:
            messages.error(request, 'Please enter a valid name.')
            return redirect('/')
        context = {
            'name' : request.POST['name'],
            'location' : request.POST['location'],
            'language' : request.POST['language'],
            'comment' : request.POST['comment']
        }
        # Increment and display a flashed message counting form submissions
        request.session['count'] += 1
        messages.success(request, 'Thank you for your submission. You have now completed this form {} times.'.format(request.session['count']))
        # Render the result page displaying the submitted form values
        return render(request, 'main_app/result.html', context)
    else:
        return redirect('/')

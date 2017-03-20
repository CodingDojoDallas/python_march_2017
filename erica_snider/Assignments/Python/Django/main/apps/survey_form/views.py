from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey_form/index.html')


def process(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def results(request):
    return render(request, 'survey_form/results.html')

def goback(request):
    return redirect('/')

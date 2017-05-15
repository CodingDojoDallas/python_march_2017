from django.shortcuts import render
import random


# CONTROLLER


# Create your views here.

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    print "*"*50
    generated_number = random.randint(10000000000000, 100000000000000)
    context = {
        'generated_number': generated_number
    }
    # del request.session['count']
    return render(request, 'word_generator/index.html',context)

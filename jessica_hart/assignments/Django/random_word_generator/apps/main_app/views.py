from django.shortcuts import render, redirect, HttpResponse
import random
import string

# Create your views here.
def index(request):
    # Generates session values if not existing
    if not 'count' in request.session:
        request.session['count'] = 0
    if not 'string' in request.session:
        request.session['string'] = ' '
    return render(request, 'main_app/index.html')

def generate(request):
    if request.method == 'POST':
        # Generate 14 character string of random 0-9 A-Z
        rand_str = string_generator(14, string.ascii_uppercase + string.digits)
        request.session['string'] = rand_str
        request.session['count'] += 1
        return redirect('/')
    else:
        return redirect('/')

def string_generator(size, chars):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
    # Alternative: ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

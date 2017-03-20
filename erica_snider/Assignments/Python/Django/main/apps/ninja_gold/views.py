from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
    return render(request, 'index.html')

def process_money(request):
    win_lose = 1 # winning gold
    building = request.POST['building']
    if building == 'farm':
        request.session['gold'] = random.randrange(10,21)
        building = request.POST['building']
    elif building == 'cave':
        request.session['gold'] = random.randrange(5,11)
    elif building == 'house':
        request.session['gold'] = random.randrange(2,6)
    elif building == 'casino':
        request.session['gold'] = random.randrange(0,51)
        earn_or_take = random.randrange(0,2)
        if earn_or_take == 0:
            request.session['gold'] *= -1
            win_lose = 0 # losing gold
    print request.session['gold']
    request.session['total_gold'] += request.session['gold']

    if win_lose == 1:
        request.session['activity_log'].append("Earned " + str(request.session['gold']) + " golds from the " + building + "!")
    else:
        request.session['activity_log'].append("Entered a casino and lost " + str(request.session['gold']*-1) + " golds... Ouch.. ")

    return redirect('/')

def reset(request):
    request.session.pop('activity_log')  # Check on pop in django
    request.session.pop('total_gold')  # Check on pop in django
    return redirect('/')

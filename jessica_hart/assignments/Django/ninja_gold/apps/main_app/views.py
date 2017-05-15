from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if not 'gold' in request.session:           # If no gold is in session, set gold to 0
        request.session['gold'] = 0
    if not 'events' in request.session:         # Initialize events list if not in session
        request.session['events'] = []
    return render(request, 'main_app/index.html')

def process_farm_gold(request):
    if request.method == 'POST':
        result = random.randint(10, 21)             # Generate gold range based on farm
        request.session['gold'] += result
        process_message('Farm', result, request)    # Call the message function to update activity
    return redirect('/')

def process_cave_gold(request):
    if request.method == 'POST':
        result = random.randint(5, 11)              # Generate gold range based on cave
        request.session['gold'] += result
        process_message('Cave', result, request)    # Call the message function to update activity
    return redirect('/')

def process_house_gold(request):
    if request.method == 'POST':
        result = random.randint(2, 6)               # Generate gold range based on house
        request.session['gold'] += result
        process_message('House', result, request)   # Call the message function to update activity
    return redirect('/')

def process_casino_gold(request):
    if request.method == 'POST':
        result = random.randint(-50, 51)            # Generate gold range based on casino
        request.session['gold'] += result
        process_message('Casino', result, request)  # Call the message function to update activity
    return redirect('/')

def process_message(building, result, request):     # Updates the "activity" messages with gold findings
    timestamp = datetime.now().strftime('%Y/%m/%d %-I:%S %p')
    if result < 0:
        act_string = 'Entered a {} and lost {} gold... Ouch.. ({})'.format(building, abs(result), timestamp)
        rg_class = 'red'
    else:
        act_string = 'Earned {} gold from the {}! ({})'.format(result, building, timestamp)
        rg_class = 'green'
    event = {                   # Pass both the string to print and the desired color class
        'msg': act_string,
        'class': rg_class,
    }
    request.session['events'].insert(0, event)


### Orignal before refactoring into separate routes to eliminate hidden inputs ###
# def process_gold(request):
#     if request.method == 'POST':
#         building = request.POST['building']     # Generate gold range based on building
#         if building == 'Farm':
#             result = random.randint(10, 21)
#             request.session['gold'] += result
#         elif building == 'Cave':
#             result = random.randint(5, 11)
#             request.session['gold'] += result
#         elif building == 'House':
#             result = random.randint(2, 6)
#             request.session['gold'] += result
#         elif building == 'Casino':
#             result = random.randrange(-50, 51)
#             request.session['gold'] += result
#
#         timestamp = datetime.now().strftime('%Y/%m/%d %-I:%S %p')
#         if result < 0:
#             act_string = 'Entered a {} and lost {} gold... Ouch.. ({})'.format(building, abs(result), timestamp)
#             rg_class = 'red'
#         else:
#             act_string = 'Earned {} gold from the {}! ({})'.format(result, building, timestamp)
#             rg_class = 'green'
#         event = {                   # Pass both the string to print and the desired color class
#     		'msg': act_string,
#     		'class': rg_class,
#     	}
#         request.session['events'].insert(0, event)
#     return redirect('/')

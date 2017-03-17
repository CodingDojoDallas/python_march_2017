from django.shortcuts import render,redirect
import random
import datetime

def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0
		request.session['log'] = ["Thanks for joining the game!"]
	return render(request, 'ninja_gold/index.html')

def create(request):
	time = datetime.datetime.now().strftime('(%Y/%m/%d %-I:%M %p)')
	if request._post['arena'] == 'farm':
		earnings = random.randint(10,20)
	elif request._post['arena'] == 'cave':
		earnings = random.randint(5,10)
	elif request._post['arena'] == 'house':
		earnings = random.randint(2,5)
	else:
		earnings = random.randint(-50,50)
	if earnings < 0:
		paystub = "Lost "
	else:
		paystub = "Earned "
	paystub += str(earnings) + " gold from the " + request._post['arena'] + "! " + time
	request.session['gold'] += earnings
	request.session['log'].append(paystub)
	return redirect('/')

# BONUS: to use route parameters instead of hidden inputs
# change the above 'create' method to the one below
# also see changes in urls.py and index.html files to make this work
#
# def create(request, arena):
# 	time = datetime.datetime.now().strftime('(%Y/%m/%d %-I:%M %p)')
# 	if arena == 'farm':
# 		earnings = random.randint(10,20)
# 	elif arena == 'cave':
# 		earnings = random.randint(5,10)
# 	elif arena == 'house':
# 		earnings = random.randint(2,5)
# 	else:
# 		earnings = random.randint(-50,50)
# 	if earnings < 0:
# 		paystub = "Lost "
# 	else:
# 		paystub = "Earned "
# 	paystub += str(earnings) + " gold from the " + arena + "! " + time
# 	request.session['gold'] += earnings
# 	request.session['log'].append(paystub)
# 	return redirect('/')
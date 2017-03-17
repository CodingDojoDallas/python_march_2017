from django.shortcuts import render, redirect
import random

def index(request):
	# if 'attempt' isn't in session then 'word' won't be either so no need to check for both
	if not 'attempt' in request.session:
		request.session['attempt'] = 0
		request.session['word'] = 'Click Generate Button for a Random String'
	return render(request, 'random_word/index.html')

def create(request):
	random_length = random.randint(2,12) #determine a random length for the string
	random_word = ''
	vowels = ['a','e','i','o','u','y']
	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
	for i in range(random_length):
		temp_index = random.randint(0,len(consonants)-1)
		random_word += consonants[temp_index]
		temp_index = random.randint(0,len(vowels)-1)
		random_word += vowels[temp_index]
	request.session['attempt'] += 1
	request.session['word'] = random_word
	return redirect('/')

def reset(request):
	del request.session['attempt']
	del request.session['word']
	return redirect('/')

# from django.shortcuts import render, redirect
# import random

# def index(request):
# 	# if 'attempt' isn't in session then we can assume this is the first time loading the page
# 	# so we can set both session['attempt'] and session['word']
# 	if not 'attempt' in request.session:
# 		request.session['attempt'] = 0
# 		request.session['word'] = 'Click Generate Button for a Random String'
# 	return render(request, 'random_word/index.html')

# def create(request):
# 	random_word = ''
# 	vowels = ['a','e','i','o','u','y']
# 	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
# 	for i in range(7):
# 		cons_index = random.randint(0,len(consonants)-1)
# 		random_word += consonants[cons_index]
# 		vow_index = random.randint(0,len(vowels)-1)
# 		random_word += vowels[vow_index]
# 	request.session['attempt'] += 1
# 	request.session['word'] = random_word
# 	return redirect('/')

# def reset(request):
# 	del request.session['attempt']
# 	del request.session['word']
# 	return redirect('/')
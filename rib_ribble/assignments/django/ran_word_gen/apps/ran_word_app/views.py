from django.shortcuts import render, redirect
import random

def index(request):
    if not 'count' in request.session:
        request.session["count"]= 0
    return render(request, "ran_word_app/index.html")

def create(request):
    letters = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ran_word = ""
    for i in range(14):
        temp = random.randint(0,len(letters)-1)
        ran_word += letters[temp]
    request.session["display"] = ran_word
    request.session["count"] += 1
    return redirect("/")

# Create your views here.

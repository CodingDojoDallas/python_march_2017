from django.shortcuts import render
import datetime

def index(request):
	current = {
		"time":datetime.datetime.now()
	}
	return render(request, 'timedisplay/index.html', current)

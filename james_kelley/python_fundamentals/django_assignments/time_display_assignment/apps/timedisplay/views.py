from django.shortcuts import render
from django.utils import timezone
# Create your views here.

def index(request):
	context = {
		'CurrentTime' : timezone.now()
	}
	return render(request, 'timedisplay/index.html', context)
	
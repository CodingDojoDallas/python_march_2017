from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    time = now.strftime("%b %d, %Y %-I:%M %p")
    context = {
        "time": time
    }
    return render(request, 'timedisplay/index.html', context)
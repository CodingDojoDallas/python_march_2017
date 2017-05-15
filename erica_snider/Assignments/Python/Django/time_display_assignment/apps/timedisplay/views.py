from django.shortcuts import render
import datetime, time

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    context = {
        'datetime': {   'year': now.year,
                        'month': now.month,
                        'day': now.day,
                        'hour': now.hour,
                        'minute': now.minute,
                        'second': now.second
                    }
    }
    return render(request, 'timedisplay/index.html', context)

from django.shortcuts import render
import time

def index(request):
    localtime = time.localtime(time.time())
    print localtime
    context = {
        "time": localtime
    }
    return render(request,"time_display_app/index.html", context)
# Create your views here.

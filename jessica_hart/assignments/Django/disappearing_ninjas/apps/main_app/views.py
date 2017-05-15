from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def ninjas(request, id):
    print id
    context = {
        'color': id
    }
    return render(request, 'main_app/ninjas.html', context)

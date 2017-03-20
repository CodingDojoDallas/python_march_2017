from django.shortcuts import render

# Create your views here.
def index(request):
    request.session['ninjas'] = {
        'blue': 'donatello.jpg',
        'orange': 'michelangelo.jpg',
        'red': 'raphael.jpg',
        'purple': 'leonardo.jpg'
    }
    return render(request, 'index.html')

def ninjas(request):
    # request.session['color'] = ['blue','orange','red','purple']
    # print request.session['ninjas']['blue']
    context = {
        'color': request.session['ninjas']
    }

    return render(request, 'ninja.html', context)

def specific_ninja(request, color):
    # print request.session['ninjas'][color]
    print "the color is", color
    specific_color = request.session['ninjas'][color]
    print "the specific color is", specific_color
    context = {
        'color': specific_color
    }
    print "the context is", context
    print "the context['color'] is", context['color']

    for item in context['color'].items:
        print color.items

    return render(request, 'ninja.html', context)

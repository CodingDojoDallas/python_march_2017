from django.conf.urls import url
from . import views

def index(request):
    pass

urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result)
]

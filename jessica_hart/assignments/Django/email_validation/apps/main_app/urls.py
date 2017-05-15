from django.conf.urls import url
from . import views

def index(request):
    pass

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^success$', views.success),
    url(r'^remove/(?P<id>\w+)$', views.remove)
]

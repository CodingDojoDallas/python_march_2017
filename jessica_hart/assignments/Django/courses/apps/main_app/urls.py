from django.conf.urls import url
from . import views

def index(request):
    pass

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^courses/destroy/(?P<id>\w+)$', views.destroy),
    url(r'^courses/destroy/confirm/(?P<id>\w+)$', views.destroy_confirm)
]

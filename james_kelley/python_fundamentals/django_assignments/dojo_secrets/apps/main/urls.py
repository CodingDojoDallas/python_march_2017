from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.create_user),
    url(r'^login$', views.login_user),
    url(r'^secrets$', views.secrets),
    url(r'^create_secret$', views.create_secrets),
    url(r'^likes/(?P<id>\d+)$', views.likes),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^popular$', views.popular),
  
    
    
]

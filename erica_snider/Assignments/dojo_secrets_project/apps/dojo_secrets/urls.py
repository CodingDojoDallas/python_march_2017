from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^secrets$', views.secrets),
    url(r'^secrets/create$', views.create),
    url(r'^secrets/(?P<id>\d+)/like$', views.like),
    url(r'^secrets/(?P<id>\d+)/update$', views.update),
    url(r'^secrets/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^secrets/mostpopular$', views.most_popular),
    url(r'^secrets/formandrecent$', views.form_and_recent),
]

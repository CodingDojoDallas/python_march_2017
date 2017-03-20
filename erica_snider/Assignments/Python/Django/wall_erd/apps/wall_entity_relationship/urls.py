from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.create),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^message$', views.message),
    url(r'^comment$', views.comment),
    url(r'^wall$', views.wall)
]

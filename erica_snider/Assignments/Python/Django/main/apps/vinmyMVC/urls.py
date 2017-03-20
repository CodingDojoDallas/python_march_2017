from django.conf.urls import url
from . import views

urlpatterns = [   # I screwed ths up ...
    url(r'^$', views.index),
    url(r'^show/$', views.show)
]

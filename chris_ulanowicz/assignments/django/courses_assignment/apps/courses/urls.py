from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^courses/create$', views.create),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/delete/(?P<id>\d+)$', views.delete),
    url(r'^courses/edit/(?P<id>\d+)$', views.edit),
    url(r'^courses/update/(?P<id>\d+)$', views.update)
]
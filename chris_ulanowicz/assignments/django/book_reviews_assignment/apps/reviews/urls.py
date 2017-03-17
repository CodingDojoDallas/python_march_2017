from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='reviews_index'),
	url(r'^destroy/(?P<id>\d+)$', views.destroy, name='reviews_destroy'),
	url(r'^create$', views.create, name='reviews_create')
]
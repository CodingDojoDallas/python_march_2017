from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='books_index'),
	url(r'^add$', views.new, name='books_new'),
	url(r'^create$', views.create, name='books_create'),
	url(r'^(?P<id>\d+)$', views.show, name='books_show')
]
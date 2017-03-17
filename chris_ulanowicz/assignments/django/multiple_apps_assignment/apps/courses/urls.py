from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='course_index'),
	url(r'^courses/create$', views.create, name='course_create'),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name='course_destroy'),
    url(r'^courses/delete/(?P<id>\d+)$', views.delete, name='course_delete'),
    url(r'^courses/edit/(?P<id>\d+)$', views.edit, name='course_edit'),
    url(r'^courses/update/(?P<id>\d+)$', views.update, name='course_update'),
    url(r'^courses/join/(?P<id>\d+)$', views.join, name='course_join')
]
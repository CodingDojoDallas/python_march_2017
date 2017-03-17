from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^process_money$', views.create)
]

# BONUS: to use route parameters instead of hidden inputs
# change the above urlpatterns code to below
# also see changes in views.py file and index.html file to make this work
# 
# urlpatterns = [
# 	url(r'^$', views.index),
# 	url(r'^process_money/(?P<arena>\w+)$', views.create)
# ]
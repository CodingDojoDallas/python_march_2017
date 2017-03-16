from django.conf.urls import url
from . import views

def index(request):
    pass

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_farm_gold$', views.process_farm_gold),
    url(r'^process_cave_gold$', views.process_cave_gold),
    url(r'^process_house_gold$', views.process_house_gold),
    url(r'^process_casino_gold$', views.process_casino_gold)
]

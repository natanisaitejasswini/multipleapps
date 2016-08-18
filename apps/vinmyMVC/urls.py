from django.conf.urls import url 
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.create),
    url(r'^reset$', views.gold_refresh)
]
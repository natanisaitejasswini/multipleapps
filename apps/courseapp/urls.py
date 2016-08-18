from django.conf.urls import url 
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^course$', views.user),
    url(r'^select_page/(?P<id>\d+)$', views.deletepage),
    url(r'^yes/(?P<id>\d+)$', views.selectyes),
    url(r'^no$', views.index),
  
]
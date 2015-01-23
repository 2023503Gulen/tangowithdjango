from django.conf.urls import patterns,url
from rango import views

urlpatterns = pattern('', url(r'^$', views.index, name='index'))

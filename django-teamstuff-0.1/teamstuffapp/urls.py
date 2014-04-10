from django.conf.urls import patterns, url
from teamstuffapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

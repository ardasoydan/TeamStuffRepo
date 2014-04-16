from django.conf.urls import patterns, url
from teamstuffapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^$', views.login, name = 'login'),
    url(r'^$', views.signup, name = 'signup'),

)

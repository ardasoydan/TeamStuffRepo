from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TeamStuff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/','teamstuffapp.views.index'),
    url(r'^login/', 'teamstuffapp.views.login'),
    url(r'^signup/', 'teamstuffapp.views.signup'),
)

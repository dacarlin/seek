from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from enter import views
from enter.models import EntryForm

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^browse/', views.browse, name='browse'),
    url(r'^adam/$', views.adam),
    url(r'^thanks/$', views.thanks),
    url(r'^help/', views.help),
    )

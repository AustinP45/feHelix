from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.categorys_list),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category_detail),
)
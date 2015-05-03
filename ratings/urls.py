# import django modules
from django.conf.urls import patterns, include, url

# import Views
from . import views

# define regex matches for URLs
urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^categories$', views.categorys_list),
    url(r'^nominate_category$', views.nominate_category),
    url(r'^nominate_tool$', views.nominate_tool),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category_detail),
    url(r'^category/(.+)/$', views.category_detail_by_name),
    url(r'^tool/(.+)/$', views.tool_detail_by_name),
    url(r'^tool/(?P<pk>[0-9]+)/$', views.tool_detail),
)

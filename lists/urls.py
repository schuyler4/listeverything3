from django.conf.urls import include, url
from . import views

urlpatterns = [ 
	url(r'^$', views.index, name="index"),
	url(r'^addlist/$', views.add_list, name="add"),
	url(r'^(?P<title>.+?)/list/$', views.list, name="list"),
	url(r'^listalllists/$', views.list_all, name="list_all")
]
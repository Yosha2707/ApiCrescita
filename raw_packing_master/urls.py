from django.conf.urls import url, include
from . import views
from .views import rawList, rawCreate, rawUp, delete, get_place 



urlpatterns = [
url(r'^$', views.rawList.as_view(), name='post_list'),
url(r'^create$', views.rawCreate.as_view(), name='post_create'),
url(r'^(?P<pk>\d+)/$', views.rawUp.as_view(), name='post_up'),
#url(r'^delete/(?P<pk>\d+)/$', views.delete , name='delete'),
url(r'^autor', views.get_place, name='autor'),


]
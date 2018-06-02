from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import modeUp , modeCreate, modeList, ModeFileUpload




urlpatterns = [

url(r'^$', views.modeList.as_view(), name='post_list'),
url(r'^create$', views.modeCreate.as_view(), name='post_create'),
url(r'^file$', views.ModeFileUpload.as_view(), name='post_file'),
url(r'^(?P<pk>\d+)/$', views.modeUp.as_view(), name='post_rud')
]



from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import manuList, ManuUp


#router = routers.DefaultRouter()
#router.register(r'costpack', manuList2, base_name='manuList2')

urlpatterns = [
#url(r'^', include(router.urls)),
url(r'^list$', views.manuList.as_view(), name='list'),
#url(r'^auto$', views.get_place, name='autoR'),
url(r'^(?P<pk>\d+)/$', views.ManuUp.as_view(), name='post_up'),
]
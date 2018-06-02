from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import UserViewSet, UserLoginApiView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^log$', UserLoginApiView.as_view(), name="user_login"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
]
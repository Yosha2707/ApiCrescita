
from django.conf.urls import url, include
from django.contrib import admin
import mode_master
import raw_packing_master
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_framework.authtoken import views



urlpatterns = [
	
    url(r'^admin/', admin.site.urls),
	url(r'^mode/', include('mode_master.urls')),
	url(r'^raw/', include('raw_packing_master.urls')),
	url(r'^login/', include('login.urls')),
	url(r'^manu/', include('manufacturing_cost_master.urls')),
	#url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	#url(r'^api-token-auth/$', rest_framework.authtoken.views.obtain_auth_token),

]

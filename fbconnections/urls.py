from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, url, include
from rest_framework import routers
from fbfriendsapp import views

router = routers.DefaultRouter()
router.register(r'linkedin', views.LinkedinViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'fbfriendsapp.views.index', name='index'),
    url(r'^register/$', 'fbfriendsapp.views.register', name='register'),
    url(r'^login/$', 'fbfriendsapp.views.login', name='login'),
    url(r'^home/$', 'fbfriendsapp.views.home', name='home'),
    url(r'^update/$', 'fbfriendsapp.views.update', name='update'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('social_auth.urls')),
	# (r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
)

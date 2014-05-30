from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
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

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('photoslideshow.urls')), # redirects root to our photo project
    url(r'^photoslideshow/', include('photoslideshow.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

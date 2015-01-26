from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from blogs.views import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'accordion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'accordion.views.home', name='home'),
    url(r'^blogs/$', hello),
)

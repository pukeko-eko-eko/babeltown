from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'babeltown.views.home', name='home'),
    #url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^phrasepower/', include('phrasepower.urls', namespace="phrasepower")),
    url(r'^admin/', include(admin.site.urls)),
)

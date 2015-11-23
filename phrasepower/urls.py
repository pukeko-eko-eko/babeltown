from django.conf.urls import patterns,  url

from phrasepower import views

urlpatterns = patterns('',
  
    url(r'^$', views.index, name='index'),
    url(r'^test/', views.test, name='test'),# this is just to test how URLs work
    url(r'^(?P<phrase_id>\d+)/$', views.showphrase, name='showphrase'),
    url(r'^addphrase/', views.addphrase, name='addphrase'),
    url(r'^submitphrase/', views.submitphrase, name='submitphrase'),
    
)

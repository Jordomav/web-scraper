from django.conf.urls import url

from . import views

app_name = 'scrape'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scrape/$', views.post, name='post'),
    url(r'^results/(?P<post_body>[0-9]+)/$', views.view, name='view')
]

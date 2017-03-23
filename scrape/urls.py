from django.conf.urls import url

from . import views

app_name = 'scrape'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scrape/$', views.post, name='post'),
    url(r'^(?P<post_body>.[ \w-]+)/results/$', views.scraped, name='scraped')
]

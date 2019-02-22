from django.conf.urls import url
from public import views

app_name="public"
urlpatterns = [
        url(r'^$', views.home_page, name='index'),
        url(r'^pub/first/$', views.first_comic, name='first'),
        url(r'^pub/last/$', views.last_comic, name='last'),
        url(r'^pub/(?P<slug>[-\w]+)/$', views.home_page, name='slug'),
        url(r'^pub/previous/(?P<slug>[-\w]+)/$', views.previous_comic, name='previous'),
        url(r'^pub/next/(?P<slug>[-\w]+)/$', views.next_comic, name='next'),
        ]

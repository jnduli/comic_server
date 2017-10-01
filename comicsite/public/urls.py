from django.conf.urls import url
from public import views

urlpatterns = [
        url(r'^$', views.home_page, name='index'),
        url(r'^pub/(?P<slug>[-\w]+)/$', views.home_page, name='slug'),
        url(r'^pub/previous/(?P<slug>[-\w]+)/$', views.previous_comic, name='previous'),
        url(r'^pub/next/(?P<slug>[-\w]+)/$', views.next_comic, name='next'),
        ]

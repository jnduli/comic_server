from django.conf.urls import url
from strip import views

urlpatterns = [
        url('^concept/(?P<pk>[0-9]+)/add_strip/$', views.StripCreate.as_view(), name='strip_create'),
        url('^concept/(?P<pk>[0-9]+)/edit_strip/$', views.StripUpdate.as_view(), name='strip_edit'),
        ]

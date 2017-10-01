from django.conf.urls import url
from gimp import views

urlpatterns = [
        url('^concept/(?P<pk>[0-9]+)/add_gimp/$', views.GimpCreate.as_view(), name='gimp_create'),
        url('^concept/(?P<pk>[0-9]+)/edit_gimp/$', views.GimpUpdate.as_view(), name='gimp_edit'),
        ]

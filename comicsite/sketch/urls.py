from django.conf.urls import url
from sketch import views

urlpatterns = [
        url('^concept/(?P<pk>[0-9]+)/add_sketch/$', views.SketchCreate.as_view(), name='sketch_create'),
        ]

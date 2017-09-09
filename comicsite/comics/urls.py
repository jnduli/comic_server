from django.conf.urls import url
from comics import views

urlpatterns = [
        #url(r'^$', views.system_page),
        url(r'^system/', views.system_page, name='index'), 
        url(r'^not_made/', views.page_not_made, name='not_made'),
        url(r'^detail_concept/(?P<pk>[0-9]+)/sketch_add/$', views.SketchCreate.as_view(), name='sketch_create'),
        ]

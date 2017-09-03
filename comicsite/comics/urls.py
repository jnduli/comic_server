from django.conf.urls import url
from comics import views

urlpatterns = [
        #url(r'^$', views.system_page),
        url(r'^system/', views.system_page, name='index'), 
        url(r'^not_made/', views.page_not_made, name='not_made'),
        url(r'^login/', views.login, name='login'),
        url(r'^logout/', views.logout, name='logout'),
        url(r'^add_concept/', views.ConceptCreate.as_view(), name='add_concept'),
        url(r'^list_concept/', views.ConceptList.as_view(), name='list_concept'),
        url(r'^detail_concept/(?P<pk>[0-9]+)/$', views.ConceptDetail.as_view(), name='detail_concept'),
        url(r'^detail_concept/(?P<pk>[0-9]+)/sketch_add/$', views.SketchCreate.as_view(), name='sketch_create'),
        ]

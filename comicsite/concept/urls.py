from django.conf.urls import url
from concept import views

urlpatterns = [
        url(r'^add_concept/', views.ConceptCreate.as_view(), name='add_concept'),
        url(r'^edit_concept/(?P<pk>[0-9]+)/$', views.ConceptUpdate.as_view(),name='edit_concept'),
        url(r'^list_concepts/', views.ConceptList.as_view(), name='list_concepts'),
        url(r'^concept/(?P<pk>[0-9]+)/$', views.ConceptDetail.as_view(), name='detail_concept'),
        url(r'^publish/(?P<concept_id>[0-9]+)/$', views.publish_concept, name='publish_concept'),
        ]

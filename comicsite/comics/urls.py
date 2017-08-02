from django.conf.urls import url
from comics import views

urlpatterns = [
        #url(r'^$', views.system_page),
        url(r'^system/', views.system_page, name='index'), 
        url(r'^login/', views.login, name='login'),
        ]

from django.conf.urls import url
from public import views

urlpatterns = [
        url(r'^$', views.home_page, name='index'),
        ]

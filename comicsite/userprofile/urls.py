from django.conf.urls import url
from userprofile import views

app_name="userprofile"
urlpatterns = [
        url(r'^details/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='details'),
        url(r'edit/(?P<pk>[0-9]+)$', views.UserUpdate.as_view(), name='edit'),
        ]

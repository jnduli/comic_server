from django.conf.urls import url
from userprofile import views

app_name="userprofile"
urlpatterns = [
        url(r'^details/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='details'),
        ]

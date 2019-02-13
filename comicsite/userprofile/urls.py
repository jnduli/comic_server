from django.conf.urls import url
from userprofile import views

app_name="userprofile"
urlpatterns = [
        url(r'^details/', views.UserDetail.as_view(), name='details'),
        ]

from django.conf.urls import url
from authenticate import views

app_name="authenticate"
urlpatterns = [
        url(r'^login/', views.login, name='login'),
        url(r'^logout/', views.logout, name='logout'),
        ]

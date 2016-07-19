from django.conf.urls import patterns, url
from . import views
urlpatterns = (
        url(r'^login$', views.login, name='login'),
        url(r'^logout$', views.logout_view, name='logout'),
        )

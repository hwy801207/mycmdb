from django.conf.urls import url

from . import views

urlpatterns =[ 
        url(r'^chpasswd/$', views.chpasswd, name="chpasswd"),
        url(r'^auth/$', views.ldap_auth, name="auth"),
        url(r'^success/$', views.success, name='success'),
        ]

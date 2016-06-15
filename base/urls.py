from django.conf.urls import url
from .views import upload, download
urlpatterns =[
             url(r'^upload$', upload, name="upload"), 
             url(r'^download$', download, name="download"),
              ] 

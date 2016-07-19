from django.conf.urls import url
from .views import upload, download
from .views import modifyServer, addServer, delServer, getServer 

urlpatterns =[
             url(r'^upload$', upload, name="upload"), 
             url(r'^download$', download, name="download"),
             url(r'^modify$', modifyServer, name="modifyserver" ),
             url(r'^add$', addServer, name="addserver"),
             url(r'^del/(\d+)$', delServer, name="delserver"),
             url(r'^list$', getServer, name="listserver"),
             ] 

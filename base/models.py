from django.db import models

from django.contrib import admin


class Resource(models.Model):
    username = models.CharField(max_length=64)
    file_path = models.FileField(upload_to="./upload/")
    
    
    def __unicode__(self):
        return self.username
    
    
    class Admin:
        pass
     
    class Meta:
        db_table = "resource"
    
    
admin.site.register(Resource)
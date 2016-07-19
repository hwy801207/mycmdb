from django.contrib import admin

from .models import Server, Resource
# Register your models here.

admin.site.register(Server)
admin.site.register(Resource)

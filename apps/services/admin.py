from django.contrib import admin

from .models import *

class ServiceAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['id', 'service']

class ServiceMessageAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['text' , 'id']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceMessage, ServiceMessageAdmin)

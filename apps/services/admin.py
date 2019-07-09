from django.contrib import admin

from .models import *

class ServiceAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['id', 'service']

admin.site.register(Service, ServiceAdmin)

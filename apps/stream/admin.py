from django.contrib import admin

# Register your models here.
from .models import *

class StreamAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['id','title']


admin.site.register(Stream, StreamAdmin)

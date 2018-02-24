from django.contrib import admin

from .models import *

class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class ThreadAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message']

admin.site.register(Board, BoardAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)


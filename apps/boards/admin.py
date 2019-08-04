from django.contrib import admin

from .models import *

class BoardAdmin(admin.ModelAdmin):
    """
        Displays a board's id and name
    """
    list_display = ['id','name']

admin.site.register(Board, BoardAdmin)


class ThreadAdmin(admin.ModelAdmin):
    """
        Displays a thread's y id and title
    """
    list_display = ['id','title']

admin.site.register(Thread, ThreadAdmin)


class PostAdmin(admin.ModelAdmin):
    """
        Displays a post's id and message
    """
    list_display = ['id', 'message']


admin.site.register(Post, PostAdmin)

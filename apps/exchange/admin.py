from django.contrib import admin

from .models import *

# admin.site.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['name', 'slug']
    prepopulated_fields= {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    """

    """
    list_display = ['name','slug', 'price',]
    list_filter = ['category']
    list_editable = []
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Item, ItemAdmin)

class ImageAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['id']
    List_filter = ['id']

admin.site.register(ItemImage, ImageAdmin)

from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import Product, Bookmark

# Register your models here.

class ProductAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
    ordering = ['id']
    list_display = ('id' , 'name', 'company')
    search_fields = ['id', 'name']

class BookmarkAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('user', 'product')

admin.site.register(Product, ProductAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
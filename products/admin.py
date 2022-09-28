from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import Product

# Register your models here.

class ProductAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
    ordering = ['id']
    list_display = ('id' , 'name', 'company')
    search_fields = ['id', 'name']

admin.site.register(Product, ProductAdmin)
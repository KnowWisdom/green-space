from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'category', 'point')
    
@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'pick')
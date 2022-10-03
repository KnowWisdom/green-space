from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ordering = ('item_id',)
    list_display = ('item_id', 'item_category', 'point')

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    ordering = ('space_id', 'owner')
    list_display = ('space_id', 'owner')
    
@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'pick')
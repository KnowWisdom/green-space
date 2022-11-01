from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ('id', 'user', 'text', 'image')
    


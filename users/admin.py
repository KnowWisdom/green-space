from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Follow
from django.forms import Textarea
from django.db import models

class UserAdminConfig(UserAdmin):
    ordering = ('-create_dt',)
    list_display = ('user_id', 'username', 'nickname')

    fieldsets = (
        (None, {'fields': ('nickname', 'username', 'password', 'create_dt', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('open', 'point')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields' : ('nickname', 'username', 'password', 'is_active', 'is_staff')}
        ),
    )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ('id', 'to_user', 'from_user')

admin.site.register(CustomUser, UserAdminConfig)

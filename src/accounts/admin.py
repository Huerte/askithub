from django.contrib import admin
from .models import UserStatus


class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_online')
    list_filter = ('is_online',)
    search_fields = ('user__username',)

admin.site.register(UserStatus, UserStatusAdmin)
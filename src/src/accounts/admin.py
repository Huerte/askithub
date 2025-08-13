from django.contrib import admin
from .models import UserStatus, Profile, UserActivity


class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_online')
    list_filter = ('is_online',)
    search_fields = ('user__username',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
    list_filter = ('location',)
    search_fields = ('user__username', 'location')


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type')
    list_filter = ('activity_type',)
    search_fields = ('user__username', 'activity_type')

admin.site.register(UserStatus, UserStatusAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserActivity, UserActivityAdmin)
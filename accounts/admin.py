from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ServiceProvider

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'phone_number', 'address')}),
    )

class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('user__username', 'skills')

admin.site.register(User, CustomUserAdmin)
admin.site.register(ServiceProvider, ServiceProviderAdmin)

from django.contrib import admin
from .models import Category, Service

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ServiceInline]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'duration', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)

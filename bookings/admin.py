from django.contrib import admin
from .models import Booking, Review, Payment

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'service', 'provider', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('customer__username', 'service__name', 'provider__username')
    date_hierarchy = 'date'

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating', 'created_at')
    list_filter = ('rating',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'transaction_id', 'status', 'timestamp')

admin.site.register(Booking, BookingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Payment, PaymentAdmin)

from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:service_id>/', views.BookServiceView.as_view(), name='book_service'),
    path('success/', views.booking_success, name='booking_success'),
    path('accept/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('update-status/<int:booking_id>/', views.update_booking_status, name='update_booking_status'),
    path('review/<int:booking_id>/', views.add_review, name='add_review'),
]

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm
from services.models import Service
from django.contrib.auth.decorators import login_required, user_passes_test

class BookServiceView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/book_service.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = get_object_or_404(Service, pk=self.kwargs['service_id'])
        return context

    def form_valid(self, form):
        service = get_object_or_404(Service, pk=self.kwargs['service_id'])
        booking = form.save(commit=False)
        booking.customer = self.request.user
        booking.service = service
        booking.save()
        return redirect('booking_success')

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

@login_required
def accept_booking(request, booking_id):
    if request.user.role != 'provider':
        return redirect('home')
    
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.provider is None:
        booking.provider = request.user
        booking.status = 'confirmed'
        booking.save()
    return redirect('provider_dashboard')

@login_required
def update_booking_status(request, booking_id):
    if request.user.role != 'provider':
        return redirect('home')
    
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.provider == request.user:
        new_status = request.POST.get('status')
        if new_status in ['confirmed', 'completed', 'cancelled']:
            booking.status = new_status
            if new_status == 'cancelled':
                booking.cancellation_reason = request.POST.get('cancellation_reason')
            booking.save()
    return redirect('provider_dashboard')

from .forms import ReviewForm
from .models import Review

@login_required
def add_review(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Validation: Only customer can review, and only completed bookings
    if request.user != booking.customer or booking.status != 'completed':
        return redirect('customer_dashboard')
    
    # Check if review already exists
    if hasattr(booking, 'review'):
        return redirect('customer_dashboard')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.save()
            return redirect('customer_dashboard')
    else:
        form = ReviewForm()
    
    return render(request, 'bookings/add_review.html', {'form': form, 'booking': booking})

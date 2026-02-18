from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Booking
from services.models import Service, Category
from django.urls import reverse
from datetime import date, time, timedelta

User = get_user_model()

class BookingCancellationTests(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create Users
        self.customer = User.objects.create_user(username='customer', password='password', role='customer')
        self.provider = User.objects.create_user(username='provider', password='password', role='provider')
        
        # Create Category
        self.category = Category.objects.create(name='Home')

        # Create Service
        self.service = Service.objects.create(
            category=self.category,
            name='Cleaning', 
            description='House cleaning', 
            price=100.00, 
            duration=timedelta(hours=1)
        )
        
        # Create Booking
        self.booking = Booking.objects.create(
            customer=self.customer,
            service=self.service,
            provider=self.provider,
            date=date.today(),
            time=time(10, 0),
            status='confirmed',
            address='123 Test St'
        )

    def test_provider_can_cancel_booking_with_reason(self):
        self.client.login(username='provider', password='password')
        
        url = reverse('update_booking_status', args=[self.booking.id])
        data = {
            'status': 'cancelled',
            'cancellation_reason': 'Unforeseen circumstances'
        }
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) # Redirects back
        
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, 'cancelled')
        self.assertEqual(self.booking.cancellation_reason, 'Unforeseen circumstances')

    def test_provider_cannot_cancel_others_booking(self):
        other_provider = User.objects.create_user(username='other', password='password', role='provider')
        self.client.login(username='other', password='password')
        
        url = reverse('update_booking_status', args=[self.booking.id])
        data = {'status': 'cancelled', 'cancellation_reason': 'Malicious'}
        
        response = self.client.post(url, data)
        
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, 'confirmed') # Should not change
        self.assertNotEqual(self.booking.cancellation_reason, 'Malicious')

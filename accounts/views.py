from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomerRegistrationForm, ProviderRegistrationForm, ServiceProviderUpdateForm
from .models import User, ServiceProvider
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from bookings.models import Booking

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.role == User.IS_ADMIN or user.is_superuser:
            return reverse_lazy('admin_dashboard')
        elif user.role == User.IS_CUSTOMER:
            return reverse_lazy('customer_dashboard')
        elif user.role == User.IS_PROVIDER:
            return reverse_lazy('provider_dashboard')
        return reverse_lazy('home')

class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerRegistrationForm
    template_name = 'accounts/register_customer.html'

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return redirect('customer_dashboard')

class ProviderRegisterView(CreateView):
    model = User
    form_class = ProviderRegistrationForm
    template_name = 'accounts/register_provider.html'

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return redirect('provider_dashboard')

@login_required
def customer_dashboard(request):
    bookings = request.user.bookings.all().order_by('-created_at')
    return render(request, 'accounts/customer_dashboard.html', {'bookings': bookings})

@login_required
def provider_dashboard(request):
    assignments = request.user.assigned_bookings.all().order_by('-date')
    
    # Filter available bookings by the provider's skills/services
    provider_services = request.user.provider_profile.services.all()
    available_bookings = Booking.objects.filter(
        provider=None, 
        status='pending',
        service__in=provider_services
    ).distinct().order_by('-created_at')

    return render(request, 'accounts/provider_dashboard.html', {
        'assignments': assignments,
        'available_bookings': available_bookings
    })

@login_required
def provider_profile_update(request):
    if request.user.role != User.IS_PROVIDER:
        return redirect('home')
    
    provider_profile = get_object_or_404(ServiceProvider, user=request.user)
    
    if request.method == 'POST':
        form = ServiceProviderUpdateForm(request.POST, request.FILES, instance=provider_profile)
        if form.is_valid():
            form.save()
            return redirect('provider_dashboard')
    else:
        form = ServiceProviderUpdateForm(instance=provider_profile)
    
    return render(request, 'accounts/provider_profile_update.html', {'form': form})

@login_required
def admin_dashboard(request):
    if request.user.role != User.IS_ADMIN and not request.user.is_superuser:
         return redirect('home')
    
    # Stats
    total_customers = User.objects.filter(role=User.IS_CUSTOMER).count()
    total_providers = ServiceProvider.objects.count()
    active_bookings = Booking.objects.exclude(status='completed').exclude(status='cancelled').count()
    
    # Simple revenue calc (sum of completed bookings * price)
    completed_bookings = Booking.objects.filter(status='completed')
    total_revenue = sum(b.service.price for b in completed_bookings)

    # Recent Data
    recent_bookings = Booking.objects.all().order_by('-created_at')[:5]
    new_providers = ServiceProvider.objects.all().order_by('-user__date_joined')[:5]

    return render(request, 'accounts/admin_dashboard.html', {
        'total_customers': total_customers,
        'total_providers': total_providers,
        'active_bookings': active_bookings,
        'total_revenue': total_revenue,
        'recent_bookings': recent_bookings,
        'new_providers': new_providers
    })

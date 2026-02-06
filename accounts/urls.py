from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/customer/', views.CustomerRegisterView.as_view(), name='register_customer'),
    path('register/provider/', views.ProviderRegisterView.as_view(), name='register_provider'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    path('dashboard/provider/', views.provider_dashboard, name='provider_dashboard'),
    path('dashboard/provider/update/', views.provider_profile_update, name='provider_profile_update'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
]

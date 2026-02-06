from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    IS_CUSTOMER = 'customer'
    IS_PROVIDER = 'provider'
    IS_ADMIN = 'admin'
    ROLE_CHOICES = [
        (IS_CUSTOMER, 'Customer'),
        (IS_PROVIDER, 'Service Provider'),
        (IS_ADMIN, 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=IS_CUSTOMER)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider_profile')
    data_of_birth = models.DateField(null=True, blank=True)
    skills = models.TextField(help_text="Comma-separated skills")
    experience = models.IntegerField(help_text="Years of experience", default=0)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    services = models.ManyToManyField('services.Service', related_name='providers', blank=True)
    
    def __str__(self):
        return f"{self.user.username} - Provider"

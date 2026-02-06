from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ServiceProvider

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.IS_CUSTOMER
        if commit:
            user.save()
        return user

from services.models import Service

class ProviderRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    skills = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), help_text="Comma separated skills")
    experience = forms.IntegerField(min_value=0)
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select services you provide"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.IS_PROVIDER
        if commit:
            user.save()
            provider_profile = ServiceProvider.objects.create(
                user=user,
                skills=self.cleaned_data['skills'],
                experience=self.cleaned_data['experience']
            )
            provider_profile.services.set(self.cleaned_data['services'])
        return user

class ServiceProviderUpdateForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select services you provide"
    )

    class Meta:
        model = ServiceProvider
        fields = ['skills', 'experience', 'profile_picture', 'services']
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

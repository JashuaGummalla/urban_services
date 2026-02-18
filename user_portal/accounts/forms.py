from django import forms
from .models import User, Product
import re

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'phone_number', 'email', 'password', 'role']

    def clean_phone_number(self):
        num = self.cleaned_data.get('phone_number')
        if not re.fullmatch(r'\d{10}', num):
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return num

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if (len(password) < 8 or
            not re.search(r"[A-Z]", password) or
            not re.search(r"[a-z]", password) or
            not re.search(r"\d", password) or
            not re.search(r"[^\w]", password)):
            raise forms.ValidationError("Password must be at least 8 characters long and include uppercase, lowercase, a digit, and a special character.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price']

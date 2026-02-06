from django import forms
from .models import Booking
import datetime

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'id': 'id_address'}))
    latitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    longitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}), required=False)

    class Meta:
        model = Booking
        fields = ['date', 'time', 'address', 'notes', 'latitude', 'longitude']

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date <= datetime.date.today():
            raise forms.ValidationError("Booking date must be in the future.")
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time:
            start_time = datetime.time(9, 0)
            end_time = datetime.time(17, 0)
            if not (start_time <= time <= end_time):
                raise forms.ValidationError("Booking time must be between 9:00 AM and 5:00 PM.")
        return time

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} Stars") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

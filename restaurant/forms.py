from django import forms
from django.db import models
from .models import Booking
from .widgets import DatePickerInput, TimePickerInput


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'booking_name',
            'date',
            'time',
            'number_of_people'
        ]

        widgets = {
            'date': DatePickerInput(),
            'time': TimePickerInput(),
        }

from django import forms
from django.db import models
from .models import Booking
from .widgets import DatePickerInput, TimePickerInput

from django.forms import ValidationError
import datetime


def date_validation(date):
    """
    Validates the date by checkig that it is not older
    than the current date, so user cannot book in the past.
    Parameter:
    date: The date picked in the date field by the user.
    """
    if date < datetime.date.today():
        print("VALIDATOR RUNNING")
        raise ValidationError("Please pick a future date")


class BookingForm(forms.ModelForm):
    """
    Sets the fields and the widgets for the form values.
    Parameter:
    forms.ModelForm: Imports the booking form from the model
    """
    date = forms.DateField(
        validators=[date_validation],
        widget=DatePickerInput
    )

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

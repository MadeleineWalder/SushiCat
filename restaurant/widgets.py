from django import forms


class DatePickerInput(forms.DateInput):
    """
    Adds the date picker widget to the date
    field in the form.
    Parameter:
    forms.DateInput: The booking date input field.
    """
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    """
    Adds the time picker widget to the time
    field in the form.
    Parameter:
    forms.TimeInput: The booking time input field.
    """
    input_type = 'time'

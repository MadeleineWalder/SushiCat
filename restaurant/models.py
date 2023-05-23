from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError

# edit
# delete

# Create your models here.


class Booking(models.Model):
    """
    Creates the booking model database.
    Defines each field type and any attributes.
    Orders bookings by soonest booking date first.
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_name = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.date}"

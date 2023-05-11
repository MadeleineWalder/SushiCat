from django.shortcuts import render
from .models import Booking

# Create your views here.


def get_bookings_list(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render (request, 'restaurant/restaurant_bookings.html', context)

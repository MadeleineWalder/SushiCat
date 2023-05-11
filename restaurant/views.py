from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

# Create your views here.


def get_bookings_list(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'restaurant/restaurant_bookings.html', context)


def add_bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_bookings_list')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'restaurant/add_bookings.html', context)

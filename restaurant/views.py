from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.


def get_bookings_list(request):
    """
    
    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'restaurant/restaurant_bookings.html', context)


@login_required
def add_bookings(request):
    """
    Displays the Booking Form..
    Checks the form is valid.
    If not then raises errors and redirects user blank to form.
    If so saves form and redirects user to bookings page.
    """
    submitbutton = request.POST.get("submit")

    booking_name = ''
    date = ''
    time = ''
    number_of_people = ''

    form = BookingForm(request.POST)
    if form.is_valid():
        booking_exists = Booking.objects.filter(
            customer=request.user,
            date=request.POST['date'],
            time=request.POST['time']).exists()
        if booking_exists:
            raise ValidationError("Booking already exists")
        form.instance.customer = request.user
        form.save()
        return redirect('view_booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'restaurant/add_bookings.html', context)


@login_required
def edit_booking(request, booking_id):
    """
    Checks if form is valid after editing.
    Parameter:
    booking_id: The id of the booking being edited.
    """
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
    submitbutton = request.POST.get("submit")

    booking_name = ''
    date = ''
    time = ''
    number_of_people = ''

    form = BookingForm(request.POST, instance=booking)
    if form.is_valid():
        booking_exists = Booking.objects.filter(
            customer=request.user,
            date=request.POST['date'],
            time=request.POST['time']).exists()
        if booking_exists:
            raise ValidationError("Booking already exists")
        form.instance.customer = request.user
        form.save()
        return redirect('view_booking')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'restaurant/edit_booking.html', context)


def delete_booking(request, booking_id):
    """

    """
    print(request)
    print(booking_id)
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('view_booking')


def view_booking(request):
    """

    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'restaurant/view_booking.html', context)


def menu(request):
    """

    """
    return render(request, 'restaurant/menu.html')

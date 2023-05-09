from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Booking

# Create your views here.


class BookingList(ListView):
    model = Booking
    template_name = 'index.html'

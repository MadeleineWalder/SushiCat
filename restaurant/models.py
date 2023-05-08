from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# date
# time 
# no. of people
# edit 
# delete


# Create your models here.
class Booking(models.Model):
    booking_name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()


# class Edit(models.Model):


# class Delete(models.Model):

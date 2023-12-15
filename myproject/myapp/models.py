from django.db import models

# Create your models here.
class Reservation(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    contact = models.CharField('Phone Number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300)
    booking_time = models.DateTimeField(auto_now=True)

    # Over write the Object representation(custom)
    def __str__(self):
        return self.first_name
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


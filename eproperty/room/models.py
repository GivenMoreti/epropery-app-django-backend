from django.db import models

# Create your models here.
ROOM_TYPE= (
    ("Estate","Estate"),
    ("Rent","Rent")
)

ROOM_NUMBER = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4")
)

ROOM_NAME = (
    ("AA","AA"),
    ("BB","BB"),
    ("CC","CC")
)
class Room(models.Model):
    number = models.CharField(max_length=5,choices=ROOM_NUMBER,null=True, blank=True)
    name = models.CharField(max_length=30,choices=ROOM_NAME,null=True, blank=True)
    rent = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=300)
    type = models.CharField(max_length=300,choices=ROOM_TYPE)
    images = models.FileField()

    def __str__(self):
        return self.name + " " + str(self.number)
import datetime 
# ADD A NEW CUSTOMER
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=30)
    customer_room = models.ForeignKey(Room, null=True, blank=True,on_delete=models.CASCADE)
    customer_location = models.CharField(max_length=300)
    booking_days = models.DateTimeField()
    date_added =models.DateTimeField(auto_now_add=True)


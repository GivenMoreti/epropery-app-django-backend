from django.db import models
from datetime import date
from django.contrib.auth.models import User

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


class Agent(models.Model):
    agent_name = models.CharField(max_length=30)
    agent_email = models.EmailField()
    agent_cell = models.IntegerField()


    def __str__(self):
        return self.agent_name
    # rooms agent is responsible for.
    # agent_rooms = models.

class Room(models.Model):
    # title = models.CharField(max_length=100)
    # bedrooms = models.PositiveIntegerField()
    # bathrooms = models.PositiveIntegerField()
    # available = models.BooleanField(default=True)
    # location = models.CharField(max_length=100)
    number = models.CharField(max_length=5,choices=ROOM_NUMBER,null=True, blank=True)
    name = models.CharField(max_length=30,choices=ROOM_NAME,null=True, blank=True)
    rent = models.FloatField(null=True, blank=True)
    description = models.TextField(max_length=300)
    room_type = models.CharField(max_length=300,choices=ROOM_TYPE)
    images = models.FileField()
    agent = models.ForeignKey(Agent, null=True, blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.name + " " + str(self.number)
    

# ADD A NEW CUSTOMER
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=30)
    customer_room = models.ForeignKey(Room, null=True, blank=True,on_delete=models.CASCADE)
    customer_location = models.CharField(max_length=300)
    booking_days = models.DateTimeField()
    date_added =models.DateTimeField(auto_now_add=True)

# user rental
class Rental(models.Model):
    property = models.ForeignKey(Room, on_delete=models.CASCADE)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()



class Amenities(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name




class PropertyAmenities(models.Model):
    property = models.ForeignKey(Room, on_delete=models.CASCADE)
    amenities = models.ForeignKey(Amenities, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.property.title} - {self.amenities.name}"


class Booking(models.Model):
    property = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


    def __str__(self):
        return f"{self.property.title} - {self.guest.username}"

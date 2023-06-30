from django.db import models
from location_field.models.plain import PlainLocationField
from django.forms import ModelForm
# CHOICES = (
#   ('vacant_land', 'land'),
#   ('House', 'House'),
#   ('Farm', 'Farm'),
#   ('Apartment', 'Apartment'),
#   ('Student', 'Student'),
#   ('Industrial', 'Industrial'),
#   ('Townhouse', 'Townhouse'),


# )
# Create your models here.
class Room(models.Model):
  name= models.CharField(max_length=30)
  is_available = models.BooleanField(default=True)
  rooms = models.IntegerField(default=1)
  bedrooms = models.IntegerField(default=1)
  rent = models.FloatField()
  location = PlainLocationField(based_fields=['city'], zoom=7)
  surrounding_surburb = models.CharField(max_length=30)
  has_garage = models.BooleanField(default=False)
  area = models.FloatField()
  image = models.CharField(max_length=8000,default=None)


class SearchModel(models.Model):
  query = models.CharField(max_length=300)


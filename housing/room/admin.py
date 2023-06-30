from django.contrib import admin

# Register your models here.
from .models import Room

class RoomAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_available', 'rooms','bedrooms','rent','location','surrounding_surburb','has_garage','area',)

admin.site.register(Room,RoomAdmin)
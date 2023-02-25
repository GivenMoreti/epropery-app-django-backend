from django.contrib import admin

# Register your models here.
from . models import Room,Customer

class RoomAdmin(admin.ModelAdmin):
    list_display = ("name","number","rent" ,"description","type","images")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name","customer_email","customer_room","booking_days")

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Room,RoomAdmin)
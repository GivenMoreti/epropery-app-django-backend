from django.contrib import admin
from . models import Room,Customer,Agent,Rental,Amenities,PropertyAmenities,Booking

class RoomAdmin(admin.ModelAdmin):
    list_display = ("name","number","rent" ,"description","room_type","images")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name","customer_email","customer_room","booking_days")

class AgentAdmin(admin.ModelAdmin):
    list_display = ("agent_name","agent_cell","agent_email")


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Rental)
admin.site.register(Amenities)
admin.site.register(PropertyAmenities)
admin.site.register(Booking)
from django.shortcuts import render

# Create your views here.

from .models import Room,Customer
def get_rooms(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Room.objects.create(images=image)
    rooms = Room.objects.all()
    customers = Customer.objects.all()

    context= {'rooms': rooms,
    'customers':customers}
    return render(request, 'room/index.html',context)
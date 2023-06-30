from django.shortcuts import render

# Create your views here.
# this is an app to advertise your property
from .models import Room,Customer,Agent
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

# homepage

def home(request):
    rooms = Room.objects.all()
    customers = Customer.objects.all()
    agents = Agent.objects.all()
    context = {
        'rooms':rooms,
        'customers':customers,
        'agents':agents
    }
    return render(request,'room/home.html',context)

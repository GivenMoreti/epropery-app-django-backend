from django.shortcuts import render
from .models import Room
from django.contrib import messages
# Create your views here.

from .forms import SearchFormTwo
from .models import SearchModel
# all the available rooms in a room list
def get_rooms(request):
  rooms = Room.objects.all()
  count_rooms = Room.objects.count()
  return render(request, 'room/rooms.html',
   {'rooms': rooms,
   'count_rooms':count_rooms
   })
# located in berea
# located in johannesburg
  # if
# if request.method == 'GET':
#   query_string =Room.request.get
#   contains_filter = Room.objects.filter(contains=query_string)
  





# rooms less than R1000 rent
def cheaper_rooms(request):
  cheaper_rooms = Room.objects.filter(rent__lte= 1000)
  return render(request, 'room/cheaper_rooms.html', {'cheaper_rooms':cheaper_rooms})

# these are the rooms with more than one
def more_rooms(request):
  more_rooms = Room.objects.filter(rooms__gt=1)
  return render(request, 'room/more_rooms.html', {'more_rooms':more_rooms})

def search_query(request):
  if request.method == 'POST':
    form = SearchFormTwo(request.POST)
    if form.is_valid():
      query = form.cleaned_data['query']
      results = SearchModel.objects.filter(query__icontains=query)
      return render(request, 'room/search_results.html', {'results': results})
  else:
    form = SearchFormTwo()
  return render(request, 'room/search.html', {'form': form})


from django.shortcuts import get_object_or_404, redirect

def cart(request):
  pass




def remove_from_cart(request, item_id):
    if 'cart' in request.session:
        cart = request.session['cart']
        if str(item_id) in cart:
            del cart[str(item_id)]
            request.session.modified = True
    return redirect('cart')


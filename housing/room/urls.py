from django.contrib import admin
from django.urls import path
from . import views
from .views import remove_from_cart

urlpatterns = [
    path('',views.get_rooms,name='rooms'),
    path('cheaper_rooms/',views.cheaper_rooms,name='cheaper_rooms'),
    path('more_rooms/',views.more_rooms,name='more_rooms'),
    path('search_query/',views.search_query,name='search_query'),

    # path('cart/add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    
]

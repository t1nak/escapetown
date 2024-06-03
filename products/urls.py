from django.urls import path
from .views import (
    travel_preference_view,
    itinerary_view,
    itinerary_list_view,
    itinerary_detail_view,
    blog_list_view,
    add_to_favorites
)

app_name = 'products'

urlpatterns = [
    path('travel-preferences/', travel_preference_view, name='travel_preference'),
    path('itineraries/', itinerary_view, name='itinerary'),
    path('itineraries/list/', itinerary_list_view, name='itinerary_list'),
    path('itineraries/<int:pk>/', itinerary_detail_view, name='itinerary_detail'),
    path('blogs/', blog_list_view, name='blog_list'),
    path('favorites/add/<str:item_type>/<int:item_id>/', add_to_favorites, name='add_to_favorites'),

]

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .models import Itinerary, BlogPost
from .forms import TravelPreferenceForm, ItineraryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Itinerary, PlaceToStay, CulturalActivity, BlogPost, Favorite
from django.utils.translation import get_language


def travel_preference_view(request):
    if request.method == 'POST':
        form = TravelPreferenceForm(request.POST)
        if form.is_valid():
            travel_preference = form.save(commit=False)
            travel_preference.user = request.user
            travel_preference.save()
            return redirect('success_url')  # Replace 'success_url' with your success page URL
    else:
        form = TravelPreferenceForm()
    return render(request, 'travel_preference_form.html', {'form': form})

# def itinerary_view(request):
#     if request.method == 'POST':
#         form = ItineraryForm(request.POST)
#         if form.is_valid():
#             itinerary = form.save(commit=False)
#             itinerary.user = request.user
#             itinerary.save()
#             return redirect('success_url')  # Replace 'success_url' with your success page URL
#     else:
#         form = ItineraryForm()
#     return render(request, 'itinerary_form.html', {'form': form})
 

def blog_list_view(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})


@login_required
def itinerary_list_view(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'products/index.html', {'itineraries': itineraries})

@login_required
def itinerary_detail_view(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    language = get_language()
    return render(request, 'products/include/itinerary_detail.html', {'itinerary': itinerary, 'language': language})


@login_required
def add_to_favorites(request, item_type, item_id):
    user = request.user

    if item_type == 'itinerary':
        item = get_object_or_404(Itinerary, id=item_id)
        Favorite.objects.create(user=user, itinerary=item)
    elif item_type == 'place_to_stay':
        item = get_object_or_404(PlaceToStay, id=item_id)
        Favorite.objects.create(user=user, place_to_stay=item)
    elif item_type == 'cultural_activity':
        item = get_object_or_404(CulturalActivity, id=item_id)
        Favorite.objects.create(user=user, cultural_activity=item)
    elif item_type == 'blog_post':
        item = get_object_or_404(BlogPost, id=item_id)
        Favorite.objects.create(user=user, blog_post=item)
    
    return redirect('dashboard:index')
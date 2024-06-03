from django.contrib import admin
from .models import User, BlogPost, TravelPreference, Itinerary 
from markdownx.admin import MarkdownxModelAdmin

class ItineraryAdmin(MarkdownxModelAdmin):
    list_display = ['user', 'name', 'days', 'created_at', 'updated_at']
    fields = ['user', 'name', 'days', 'intro', 'covered_highlights', 'details', 'image', 'pdf', 'gmaps_link', 'tags']

 
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(BlogPost)
admin.site.register(TravelPreference)
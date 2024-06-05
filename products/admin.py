from django.contrib import admin
from .models import User, BlogPost, TravelPreference, Itinerary
from markdownx.admin import MarkdownxModelAdmin
from modeltranslation.admin import TranslationAdmin


class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'days', 'country', 'city', 'travel_mode', 'travel_budget', 'created_at', 'updated_at')
    fields = ('name', 'user', 'days', 'intro', 'covered_highlights', 'details', 'image', 'pdf', 'gmaps_link', 'tags', 'country', 'city', 'travel_mode', 'travel_budget', 'travel_regions')

admin.site.register(Itinerary, ItineraryAdmin)
 
admin.site.register(User)
admin.site.register(BlogPost)
admin.site.register(TravelPreference)
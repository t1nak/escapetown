from django import forms
from .models import TravelPreference, Itinerary 

class TravelPreferenceForm(forms.ModelForm):
    class Meta:
        model = TravelPreference
        fields = ['preference_data']

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['days', 'covered_highlights']

 
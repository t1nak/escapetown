# translation.py

from modeltranslation.translator import translator, TranslationOptions
from .models import Itinerary

class ItineraryTranslationOptions(TranslationOptions):
    fields = ('name', 'intro', 'covered_highlights', 'details')

translator.register(Itinerary, ItineraryTranslationOptions)
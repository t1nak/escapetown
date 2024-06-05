from django.test import TestCase
from django.utils.translation import activate
from django.conf import settings
from products.models import Itinerary
from accounts.models import User  # Import the custom user model

class ItineraryTranslationTests(TestCase):

    def setUp(self):
        # Create a user for the foreign key relationship
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create an itinerary with the user
        self.itinerary = Itinerary.objects.create(
            name="Sample Itinerary",
            intro="This is a sample introduction.",
            covered_highlights="These are sample highlights.",
            details="These are sample details.",
            days=5,  # Assuming `days` is an integer field with a NOT NULL constraint
            user=self.user  # Add the user
        )

    def test_itinerary_translation(self):
        # Set up initial data in default language
        self.assertEqual(self.itinerary.name, "Sample Itinerary")
        self.assertEqual(self.itinerary.intro, "This is a sample introduction.")
        self.assertEqual(self.itinerary.covered_highlights, "These are sample highlights.")
        self.assertEqual(self.itinerary.details, "These are sample details.")

        # Activate German translation
        activate('de')
        self.itinerary.name = "Beispiel Reiseroute"
        self.itinerary.intro = "Dies ist eine Beispiel-Einführung."
        self.itinerary.covered_highlights = "Dies sind Beispiel-Highlights."
        self.itinerary.details = "Dies sind Beispiel-Details."
        self.itinerary.save()

        # Fetch the updated object to verify translations
        translated_itinerary = Itinerary.objects.get(pk=self.itinerary.pk)
        self.assertEqual(translated_itinerary.name, "Beispiel Reiseroute")
        self.assertEqual(translated_itinerary.intro, "Dies ist eine Beispiel-Einführung.")
        self.assertEqual(translated_itinerary.covered_highlights, "Dies sind Beispiel-Highlights.")
        self.assertEqual(translated_itinerary.details, "Dies sind Beispiel-Details.")

        # Switch back to the default language and verify
        activate('en')
        untranslated_itinerary = Itinerary.objects.get(pk=self.itinerary.pk)
        self.assertEqual(untranslated_itinerary.name, "Sample Itinerary")
        self.assertEqual(untranslated_itinerary.intro, "This is a sample introduction.")
        self.assertEqual(untranslated_itinerary.covered_highlights, "These are sample highlights.")
        self.assertEqual(untranslated_itinerary.details, "These are sample details.")

    def tearDown(self):
        self.itinerary.delete()
        self.user.delete()
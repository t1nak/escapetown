from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import   Itinerary, Favorite

User = get_user_model()
 

class ItineraryModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.first_name = 'Test'
        self.user.last_name = 'User'
        self.user.save()
        
        self.itinerary = Itinerary.objects.create(
            user=self.user,
            name='Test Itinerary',
            days=3,
            intro='This is a test itinerary.',
            covered_highlights='Test highlights',
            details='Test details'
        )

    def test_itinerary_creation(self):
        self.assertEqual(self.itinerary.name, 'Test Itinerary')
        self.assertEqual(self.itinerary.days, 3)
        self.assertEqual(self.itinerary.intro, 'This is a test itinerary.')
        self.assertEqual(self.itinerary.covered_highlights, 'Test highlights')
        self.assertEqual(self.itinerary.details, 'Test details')
        self.assertEqual(self.itinerary.user, self.user)

    def test_itinerary_str(self):
        self.assertEqual(str(self.itinerary), 'Test Itinerary (3-Day) for Test User')

    def tearDown(self):
        self.itinerary.delete()
        self.user.delete()

class FavoriteModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.first_name = 'Test'
        self.user.last_name = 'User'
        self.user.save()

        self.itinerary = Itinerary.objects.create(
            user=self.user,
            name='Test Itinerary',
            days=3,
            intro='This is a test itinerary.',
            covered_highlights='Test highlights',
            details='Test details'
        )
        self.favorite = Favorite.objects.create(
            user=self.user,
            itinerary=self.itinerary
        )

    def test_favorite_creation(self):
        self.assertEqual(self.favorite.user, self.user)
        self.assertEqual(self.favorite.itinerary, self.itinerary)

    def test_favorite_str(self):
        self.assertEqual(str(self.favorite), 'Favorite of testuser')

    def tearDown(self):
        self.favorite.delete()
        self.itinerary.delete()
        self.user.delete()
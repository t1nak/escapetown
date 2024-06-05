# landing_page/tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse

class LandingPageTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('landing_page:index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page/index.html')

    def test_nav_view(self):
        response = self.client.get(reverse('landing_page:nav'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing_page/nav.html')
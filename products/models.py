from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from markdownx.models import MarkdownxField
from django.utils.translation import gettext_lazy as _


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def __str__(self):
        return f"Favorite of {self.user.username}"

class TravelPreference(models.Model):
 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    preference_data = models.JSONField()  # Store preferences as JSON for flexibility
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Preferences for {self.user.first_name} {self.user.last_name}"


class Itinerary(models.Model):
    DAYS_CHOICES = [
        (3, '3-Day'),
        (5, '5-Day'),
        (7, '7-Day'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    days = models.IntegerField(choices=DAYS_CHOICES)
    intro = models.TextField()  # New intro field
    covered_highlights = MarkdownxField(default='')
    details = MarkdownxField(default='')  
    image = models.ImageField(upload_to='itinerary_images/', blank=True, null=True)
    pdf = models.FileField(upload_to='itinerary_pdfs/', blank=True, null=True)
    gmaps_link = models.URLField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Itinerary")
        verbose_name_plural = _("Itineraries")

    def __str__(self):
        return f"{self.name} ({self.get_days_display()}) for {self.user.get_full_name()}"

class PlaceToStay(models.Model):
    # existing fields
 
    pass
class CulturalActivity(models.Model):
    # existing fields
    # ...
    pass 


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, null=True, blank=True)
    place_to_stay = models.ForeignKey(PlaceToStay, on_delete=models.CASCADE, null=True, blank=True)
    cultural_activity = models.ForeignKey(CulturalActivity, on_delete=models.CASCADE, null=True, blank=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favorite of {self.user.username}"
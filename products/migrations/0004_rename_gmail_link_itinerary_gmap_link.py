# Generated by Django 4.2.7 on 2024-05-30 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_itinerary_activities_itinerary_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerary',
            old_name='gmail_link',
            new_name='gmap_link',
        ),
    ]

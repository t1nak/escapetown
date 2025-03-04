# Generated by Django 4.2.7 on 2024-05-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='gmail_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='itinerary_images/'),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='itinerary_pdfs/'),
        ),
    ]

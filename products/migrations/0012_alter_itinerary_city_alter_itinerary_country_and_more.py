# Generated by Django 4.2.7 on 2024-06-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_itinerary_covered_highlights_nl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='city',
            field=models.CharField(default='Cape Town', max_length=255),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='country',
            field=models.CharField(default='South Africa', max_length=255),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='travel_budget',
            field=models.CharField(choices=[('economy', 'Economy'), ('business', 'Business')], default='economy', max_length=10),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='travel_mode',
            field=models.CharField(choices=[('solo', 'Solo'), ('couple', 'Couple'), ('family', 'Family'), ('other', 'Other')], default='solo', max_length=10),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='travel_regions',
            field=models.TextField(blank=True, default='Cape Town central'),
        ),
    ]

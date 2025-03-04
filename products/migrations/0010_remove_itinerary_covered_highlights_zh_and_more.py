# Generated by Django 4.2.7 on 2024-06-04 18:07

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_itinerary_covered_highlights_de_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='covered_highlights_zh',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='details_zh',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='intro_zh',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='name_zh',
        ),
        migrations.AddField(
            model_name='itinerary',
            name='covered_highlights_de',
            field=markdownx.models.MarkdownxField(default='', null=True),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='details_de',
            field=markdownx.models.MarkdownxField(default='', null=True),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='intro_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='name_de',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# Generated by Django 4.2.16 on 2024-09-25 15:05

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_remove_destination_image_url_destination_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]

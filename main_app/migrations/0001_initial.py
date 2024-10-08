# Generated by Django 4.2.16 on 2024-09-22 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('O', 'Other'), ('B', 'Beach / Island'), ('W', 'Waterfall'), ('H', 'Hill / Mountain / Cliff'), ('P', 'Park / Forest / Cave'), ('E', 'Entertainment/Amusement Park'), ('Z', 'Zoo / Wildlife Attraction'), ('M', 'Museum / Art Gallery / Market / Festivals & Parades / Exhibition'), ('H', 'Historical/Heritage Attraction'), ('L', 'Landmark / Unique Built Attraction')], default='O', max_length=1)),
                ('country', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=0)),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

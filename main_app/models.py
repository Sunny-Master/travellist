from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

D_Types = (
  ('O', 'Other')
  ('B', 'Beach / Island'),
  ('W', 'Waterfall'),
  ('H', 'Hill / Mountain / Cliff'),
  ('P', 'Park / Forest / Cave'),
  ('E', 'Entertainment/Amusement Park'),
  ('Z', 'Zoo / Wildlife Attraction'),
  ('M', 'Museum / Art Gallery / Market / Festivals & Parades / Exhibition'),
  ('H', 'Historical/Heritage Attraction'),
  ('L', 'Landmark / Unique Built Attraction')
)

# Destination model
class Destination(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(
    max_length=1,
    choices=D_Types,
    default=D_Types[0][0]
  )
  country = CountryField()
  rating = models.IntegerField(default=0)
  image_url = models.URLField(
    max_length=500,
    blank=True,
    null=True
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def __str__(self.type):
    return self.get_type_display()
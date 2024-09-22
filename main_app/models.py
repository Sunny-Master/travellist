from django.db import models
from django.contrib.auth.models import User

D_TYPES = (
  ('O', 'Other'),
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
    choices=D_TYPES,
    default=D_TYPES[0][0]
  )
  country = models.CharField(max_length=100)
  rating = models.IntegerField(default=0)
  image_url = models.URLField(
    max_length=500,
    blank=True,
    null=True
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

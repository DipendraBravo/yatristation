from django.db import models
# Create your models here.


class Destination(models.Model):
	name = models.CharField(max_length=200)
	photo = models.ImageField(upload_to="photos/Destinations",blank=True)
	country = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	review = models.IntegerField()
	day_count = models.CharField(max_length=200)
def __str__(self):
    return self.name
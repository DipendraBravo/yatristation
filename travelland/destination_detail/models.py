from django.db import models
from destination.models import Destination
# Create your models here.

class Destination_detail(models.Model):
	destination = models.OneToOneField(Destination, on_delete=models.CASCADE)
	description = models.TextField()
	day1 = models.IntegerField()
	day1description = models.TextField(blank=True)
	day2 = models.IntegerField()
	day2description = models.TextField(blank=True)
	day3 = models.IntegerField()
	day3description = models.TextField(blank=True)
	day4 = models.IntegerField()
	day4description = models.TextField(blank=True)
	day5 = models.IntegerField()
	day5description = models.TextField(blank=True)
	day6 = models.IntegerField()
	day6description = models.TextField(blank=True)
	day7 = models.IntegerField()
	day7description = models.TextField(blank=True)
	day8 = models.IntegerField()
	day8description = models.TextField(blank=True)
	day9 = models.IntegerField()
	day9description = models.TextField(blank=True)
	day10 = models.IntegerField()
	day10description = models.TextField(blank=True)
def __str__(self):
    return self.id

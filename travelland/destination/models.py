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
    	return self.photo


class Destination_detail(models.Model):
	destination = models.OneToOneField(Destination, on_delete=models.CASCADE)
	description = models.TextField()
	day1 = models.CharField(max_length=255, blank=True)
	day1description = models.TextField(blank=True)
	day2 = models.CharField(max_length=255, blank=True)
	day2description = models.TextField(blank=True)
	day3 = models.CharField(max_length=255, blank=True)
	day3description = models.TextField(blank=True)
	day4 = models.CharField(max_length=255, blank=True)
	day4description = models.TextField(blank=True)
	day5 = models.CharField(max_length=255, blank=True)
	day5description = models.TextField(blank=True)
	day6 = models.CharField(max_length=255, blank=True)
	day6description = models.TextField(blank=True)
	day7 = models.CharField(max_length=255, blank=True)
	day7description = models.TextField(blank=True)
	day8 = models.CharField(max_length=255, blank=True)
	day8description = models.TextField(blank=True)
	day9 = models.CharField(max_length=255, blank=True)
	day9description = models.TextField(blank=True)
	day10 = models.CharField(max_length=255, blank=True)
	day10description = models.TextField(blank=True)
def __str__(self):
    return self.id

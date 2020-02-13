from django.db import models


# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/slider", blank=True)


def __str__(self):
    return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/sponsor", blank=True)


def __str__(self):
    return self.name


class Place(models.Model):
    photo = models.ImageField(upload_to="photos/place", blank=True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    prices = models.DecimalField(max_digits=20, decimal_places=2)
    review = models.IntegerField()
    day_count = models.CharField(max_length=200)


def __str__(self):
    return self.name

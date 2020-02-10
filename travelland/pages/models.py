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




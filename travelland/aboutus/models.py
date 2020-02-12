from django.db import models

# Create your models here.


class Ourstory(models.Model):
	ourstory = models.CharField(max_length=200)
	ourstorydescription = models.TextField(blank=True)
	storythumbphoto = models.ImageField(upload_to="photos/aboutus", blank=True)
def __str__(self):
    return self.ourstory


class Tourplan(models.Model):
	successfultour = models.IntegerField()
	yeartourarrange = models.IntegerField()
	happyclient = models.IntegerField()


class ProjectPartner(models.Model):
	projectpartners = models.CharField(max_length=200)
	projectpartnerphoto = models.ImageField(upload_to="photos/aboutus", blank=True)
	projectpartnername = models.CharField(max_length=200)
	projectpartnerdesc = models.TextField(blank=True)
def __str__(self):
    return self.projectpartnername
	



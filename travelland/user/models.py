from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, blank=True)
    contact = models.IntegerField(blank=True)
    address = models.CharField(max_length=30, blank=True)
    guider = models.CharField(max_length=30, blank=True)

def __str__(self):
    return self.contact


class Post(models.Model):
    user_name = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    blog_pic = models.ImageField(upload_to="photos/blog", blank=True)
    date = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title

class HomeStay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    getestimation = models.IntegerField()
    homestayname = models.CharField(max_length=200  ,blank=True)
    popularamenitities = models.TextField(blank=True)
    price = models.IntegerField()
    pricedetail = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    pannumber = models.CharField(max_length=200, blank=True)
    foodanddrinks = models.TextField(blank=True)
    guestservice = models.TextField(blank=True)
    outdoors = models.TextField(blank=True)
    accessibility = models.TextField(blank=True)
    homestaypicture = models.ImageField(upload_to="photos/User/HomeStay",blank=True)
    room1pic = models.ImageField(upload_to="photos/User/HomeStay",blank=True)
    room2pic = models.ImageField(upload_to="photos/User/HomeStay",blank=True)
    outdoorpic = models.ImageField(upload_to="photos/User/HomeStay",blank=True)
    citizenshipfront = models.ImageField(upload_to="photos/User/HomeStay",blank=True)
    citizenshipback = models.ImageField(upload_to="photos/User/HomeStay",blank=True)

def  __str__(self):
    return self.homestayname

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # homestayid = models.ForeignKey(HomeStay, on_delete=models.CASCADE)
    guestname = models.CharField(max_length=200  ,blank=True)
    guestcontact = models.CharField(max_length=200  ,blank=True)
    guestemail = models.CharField(max_length=200  ,blank=True)
    startdate = models.DateTimeField(default=datetime.now)
    enddate = models.DateTimeField(default=datetime.now)
    noofguest = models.IntegerField()
    reasonforbooking = models.CharField(max_length=200, blank=True)


def __str__(Self):
    return self.guestnumber
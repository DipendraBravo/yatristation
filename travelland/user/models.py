from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

class Notification(models.Model):
    title = models.CharField(max_length=250)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_welcome_message(sender,**kwargs):
    if kwargs.get('Created',False):
        Notification.objects.Create(user=kwargs.get('instance'),
                                    title="Welcome To YatriStation",
                                    message="Thanks gor signing up!")


from django.contrib import admin
from .models import UserProfile
from .models import Post
from .models import HomeStay
from .models import Book

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(HomeStay)
admin.site.register(Book)
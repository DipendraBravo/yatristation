from django.contrib import admin
from .models import Slider
from .models import Sponsor
from .models import PopularPlaces

# Register your models here.
admin.site.register(Slider)
admin.site.register(Sponsor)
admin.site.register(PopularPlaces)

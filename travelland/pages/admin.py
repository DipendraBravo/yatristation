from django.contrib import admin
from .models import Slider
from .models import Sponsor
from .models import Place
from .models import PopularPlaces
from .models import Hotel

# Register your models here.
admin.site.register(Slider)
admin.site.register(Sponsor)
admin.site.register(Place)

admin.site.register(PopularPlaces)
admin.site.register(Hotel)


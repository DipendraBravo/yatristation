from django.contrib import admin
from .models import Ourstory
from .models import Tourplan
from .models import ProjectPartner

# Register your models here.

admin.site.register(Ourstory)
admin.site.register(Tourplan)
admin.site.register(ProjectPartner)
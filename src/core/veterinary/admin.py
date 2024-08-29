from django.contrib import admin

# Register your models here.
from .models import System, Organ, Specie

admin.site.register(System)
admin.site.register(Organ)
admin.site.register(Specie)

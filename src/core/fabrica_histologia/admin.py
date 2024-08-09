from django.contrib import admin

# Register your models here.
from .models import System, Organ, Specie, SlideMicroscopyPost, Point

admin.site.register(System)
admin.site.register(Organ)
admin.site.register(Specie)
admin.site.register(SlideMicroscopyPost)
admin.site.register(Point)
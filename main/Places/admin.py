from django.contrib import admin


from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Place


@admin.register(Place)
class ShopAdmin(OSMGeoAdmin):
    default_zoom = 5
    point_zoom = 5
    list_display = ('author', 'title', 'description', 'location')

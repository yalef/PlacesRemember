from django.contrib import admin


from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Place


@admin.register(Place)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('author', 'title', 'description', 'location')

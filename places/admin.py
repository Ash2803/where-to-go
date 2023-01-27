
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


class PlaceAdmin(ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Place, PlaceAdmin)
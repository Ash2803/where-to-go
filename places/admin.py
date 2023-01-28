from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview', ]

    def get_preview(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="200">')

    get_preview.short_description = 'Preview'


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [
        ImageInline,
    ]

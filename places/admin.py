from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableStackedInline
from places.models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview', ]

    def get_preview(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="200">')

    get_preview.short_description = 'Preview'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, ModelAdmin):
    inlines = [
        ImageInline,
    ]

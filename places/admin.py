from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableStackedInline
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview', ]
    extra = 1

    def get_preview(self, obj):
        return format_html("<img src={} {}>", mark_safe(obj.image.url), "height=150 width=150")

    get_preview.short_description = 'Preview'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title', ]

from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title', unique=True)
    long_description = HTMLField(verbose_name='Long description', blank=True)
    short_description = models.TextField(verbose_name='Short description', blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (('title', 'short_description', 'long_description'),)


class Image(models.Model):
    image = models.ImageField(verbose_name='Image',
                              upload_to='images/',
                              blank=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images',
                              verbose_name='place')
    image_order = models.PositiveIntegerField(null=True, blank=True, default='I')

    def __str__(self):
        return f'{self.id} {self.place.title}'

    class Meta:
        ordering = ['image_order']
        unique_together = (('image', 'place',),)

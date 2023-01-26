from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    long_description = models.TextField(blank=True, verbose_name='Long description')
    short_description = models.TextField(blank=True, verbose_name='Short description')
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Image', null=True, blank=True, upload_to='images/')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='place')

    def __str__(self):
        return f'{self.id} {self.place.title}'

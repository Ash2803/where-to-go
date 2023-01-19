from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(blank=True, verbose_name='Description')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Image', null=True, blank=True, upload_to='images/')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='name', verbose_name='name')

    def __str__(self):
        return f'{self.id} {self.place.title}'

from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

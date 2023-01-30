import logging

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Upload new place information'

    def add_arguments(self, parser):
        parser.add_argument(
            '-l',
            type=str,
            help='Put the link to the place JSON file'
        )

    def handle(self, *args, **options):
        link = options['l']
        try:
            response = requests.get(link)
            response.raise_for_status()
            new_place = response.json()
        except requests.exceptions.RequestException:
            logging.error(f"{link} is not a valid url")
            exit()
        try:
            Place.objects.get(title=new_place['title'])
            print(f"Place {new_place['title']} already exists.")
        except Place.DoesNotExist:
            obj = Place.objects.create(
                title=new_place['title'],
                long_description=new_place['description_long'],
                short_description=new_place['description_short'],
                longitude=new_place['coordinates']['lng'],
                latitude=new_place['coordinates']['lat']
            )
            for image_url in new_place['imgs']:
                response = requests.get(image_url)
                file_name = image_url.split('/')[-1]
                file = ContentFile(response.content)
                image, created = Image.objects.get_or_create(place=obj, image=file_name)
                image.image.save(file_name, file)
                image.save()
            print('New place added')

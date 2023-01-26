from django.shortcuts import render

from places.models import Place, Image


def main(request):
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in Place.objects.all():
        imgages = [image for image in Image.objects.filter(place__id=place.id).values_list('image', flat=True)]
        places_geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": 'static/places/moscow_legends.json'
                }
            }
        )
    return render(request, 'index.html', {'places': places_geojson})

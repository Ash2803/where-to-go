from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from places.models import Place, Image


def main(request):
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in Place.objects.all():
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


def detail_place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    formatted_place = {
        "title": place.title,
        "imgs": [image for image in Image.objects.filter(place__id=place.id).values_list('image', flat=True)],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(formatted_place, json_dumps_params={'indent': 4, 'ensure_ascii': False})

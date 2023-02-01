from django.urls import path

from places.views import places_view, detail_place_view

urlpatterns = [
    path('', places_view, name='places'),
    path('place/<place_id>/', detail_place_view, name='place')
]

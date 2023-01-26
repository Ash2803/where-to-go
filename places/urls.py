from django.urls import path

from places.views import main, detail_place_view


urlpatterns = [
    path('', main, name='main'),
    path('places/<place_id>/', detail_place_view, name='place')
]

from django.urls import path

from places.views import main


urlpatterns = [
    path('', main, name='main'),
]

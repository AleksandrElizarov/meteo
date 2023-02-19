from django.urls import path

from .views import view_meteo_page, get_meteo_by_city

urlpatterns = [
    path('', view_meteo_page, name='view_meteo_page'),
    path('get_meteo', get_meteo_by_city, name='get_meteo'),
]

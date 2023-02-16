from django.urls import path

from .views import view_meteo_page

urlpatterns = [
    path('', view_meteo_page, name='view_meteo_page'),
]

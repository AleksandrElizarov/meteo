from django.shortcuts import render
from meteo.settings import settings


def view_meteo_page(request):
    print(f"KEY___:{settings.KEY_ACCESS_OPENWEATHER}")
    return render(request, 'meteo.html')

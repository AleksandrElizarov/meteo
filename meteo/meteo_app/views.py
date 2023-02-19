from django.shortcuts import render
from meteo.settings import settings


def view_meteo_page(request):
    return render(request, 'meteo.html')

def get_meteo_by_city(request):
    return render(request, 'meteo.html')



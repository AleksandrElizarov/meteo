from django.shortcuts import render
import requests
from loguru import logger
from meteo.settings import settings

url_find_current_weather_by_city_name = "http://api.openweathermap.org/data/2.5/find"  # Адрес для запроса погоды по городу
url_icon_weather = "http://openweathermap.org/img/wn/"
url_find_5days_weather_by_city_id = "http://api.openweathermap.org/data/2.5/forecast"
months_dict = {
    "January": "января",
    "February": "февраля",
    "March": "марта",
    "April": "апреля",
    "May": "мая",
    "June": "июня",
    "July": "июля",
    "August": "августа",
    "September": "сентября",
    "October": "октября",
    "November": "ноября",
    "December": "декабря"
}


def view_meteo_page(request):
    if request.GET.get('city_name'):
        query_city = request.GET.get('city_name')
        logger.info(f"Request weather by city name: {query_city}")
    else:
        query_city = 'Бишкек'
        logger.info(f"Request weather by DEFAULT city name: {query_city}")

    try:
        res_data_cur = requests.get(url=url_find_current_weather_by_city_name,
                                    params={'q': query_city, 'type': 'like', 'units': 'metric', 'lang': 'ru',
                                            'APPID': settings.KEY_ACCESS_OPENWEATHER})
        data_list_current_weather = res_data_cur.json()

        city_id = data_list_current_weather['list'][0]['id']
        city_name = data_list_current_weather['list'][0]['name']
        logger.info(f"Response city name from api.openweathermap: {city_name}")
        res_data_5days = requests.get(url=url_find_5days_weather_by_city_id,
                                      params={'id': city_id, 'units': 'metric', 'lang': 'ru',
                                              'APPID': settings.KEY_ACCESS_OPENWEATHER})
        data_list_5days_weather = res_data_5days.json()
        logger.info(f"Response meteo data 5 days: {data_list_5days_weather}")

        print(f"img/{data_list_current_weather['list'][0]['weather'][0]['icon']}.jpg")
        dict_weather_data_5days = {'city_name': query_city.capitalize(),
                                   'cur_icon': f"img/{data_list_current_weather['list'][0]['weather'][0]['icon']}.jpg",
                                   'cur_description': data_list_current_weather['list'][0]['weather'][0]['description'],
                                   'cur_temperature': data_list_current_weather['list'][0]['main']['temp'],
                                   'cur_pressure': data_list_current_weather['list'][0]['main']['pressure'],
                                   'cur_humidity': data_list_current_weather['list'][0]['main']['humidity'],
                                   'cur_wind_speed': data_list_current_weather['list'][0]['wind']['speed'],
                                   'cur_wind_deg': data_list_current_weather['list'][0]['wind']['deg'],
                                   }
        return render(request, 'meteo_success.html', context=dict_weather_data_5days)

    except Exception as e:
        logger.error(f"Exception, not data from response: {e}")
        return render(request, 'meteo_fail.html')

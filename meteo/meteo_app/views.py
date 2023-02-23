from django.shortcuts import render
import requests
from loguru import logger
import datetime
from meteo.settings import settings

url_find_current_weather_by_city_name = "http://api.openweathermap.org/data/2.5/find"  # Адрес для запроса погоды по городу
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

        first_day_date_str = data_list_5days_weather['list'][0]['dt_txt']
        obj_first_day_date_str = datetime.datetime.strptime(first_day_date_str, '%Y-%m-%d %H:%M:%S')
        first_day = obj_first_day_date_str.strftime('%d')
        formatted_first_month = obj_first_day_date_str.strftime('%B')
        first_month = months_dict[formatted_first_month]
        dict_weather_data_5days = {'city_name': city_name,
                                   'first_day': first_day,
                                   'first_month': first_month}

        return render(request, 'meteo_success.html', context=dict_weather_data_5days)

    except Exception as e:
        logger.error(f"Exception, not data from response: {e}")
        return render(request, 'meteo_fail.html')

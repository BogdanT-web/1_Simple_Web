from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import City
from .forms import CityForm

import requests


def HomeWeatherApp(request):

    appid = 'ae1d0e0ff3e5b55e2b7c8b178ef52784'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()  # для очистки формы при обновлении страницы

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'WeatherApp/index.html', context)


# class HomeWeatherApp(ListView):
#     model = Calc
#     template_name = 'WeatherApp/index.html'
#     context_object_name = 'posts'

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'WeatherApp'
#         return context

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Calc


class HomeWeatherApp(ListView):
    model = Calc
    template_name = 'WeatherApp/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WeatherApp'
        return context

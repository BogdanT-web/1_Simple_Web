from django.urls import path, include

from .views import *


urlpatterns = [
    # path('', HomeWeatherApp.as_view(), name='HomeWeatherApp'),
    path('', HomeWeatherApp, name='HomeWeatherApp'),
]

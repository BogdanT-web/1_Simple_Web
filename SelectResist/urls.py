from django.urls import path, include

from .views import *


urlpatterns = [
    path('', HomeSelectResist.as_view(), name='HomeSelectResist'),
]

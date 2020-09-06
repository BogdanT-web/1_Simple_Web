from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import SiteTime


class Home(ListView):
    model = SiteTime
    template_name = 'BaseApp/base.html'
    context_object_name = 'SiteTime'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SimpleWebViews'
        return context

from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Movie

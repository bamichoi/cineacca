from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    """ """

    pass

from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.VideoArt)
class VideoArtAdmin(admin.ModelAdmin):

    "VideoArt Admin Definition"

    """ """

    fieldsets = (
        (
            "Video Info",
            {
                "fields": (
                    "title",
                    "user",
                    "video",
                    "artist",
                    "duration",
                    "year",
                    "thumbnail",
                    "description",
                )
            },
        ),
    )

    list_display = ("title", "user", "artist", "rating", "views")

    list_filter = (
        "title",
        "user",
        "artist",
    )
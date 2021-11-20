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
                    "duration",
                    "year",
                    "thumbnail",
                    "poster",
                    "description",
                )
            },
        ),
        (
            "Staff info",
            {
                "fields": (
                    "director",
                    "screenwriter",
                    "casting",
                    "editor",
                    "director_of_photograpy",
                    "audio_director",
                    "music",
                    "art_director",
                    "costume_designer",
                    "makeup_artist",
                    "spacial_effect_supervisor",
                    "sound_designer",
                )
            },
        ),
    )

    list_display = ("title", "user", "director", "screenwriter", "rating", "views")

    list_filter = (
        "title",
        "user",
        "director",
        "screenwriter",
    )

from django.db import models
from django.forms import widgets
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_model
from django.utils.translation import ugettext_lazy as _
import subprocess
from time import time

class VideoArt(core_model.TimeStampedModel):

    """VideoArt Model Definition"""

    """video info field"""
    video = models.FileField(
        upload_to="videoart_files",
        null=True,
        blank=False,
    )  # seed 위해 임시로 null=True, Black=True
    thumbnail = models.ImageField(
        _("thumbnail"),
        upload_to="videoart_thumbnails",
        null=True,
        blank=False,  # seed 위해 임시로 null=True, Black=True
    )
    poster = models.ImageField(
        _("cover image"),
        upload_to="videoart_posters",
        default="default_images/default_poster.png",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.user", related_name="videoarts", on_delete=models.CASCADE
    )
    title = models.CharField(_("titolo"), max_length=300, blank=False)
    duration = models.IntegerField(_("durata"), default=0)
    description = models.TextField(_("descrizione"), max_length=1000)
    year = models.IntegerField(
        _("anno"),
        validators=[MinValueValidator(1900), MaxValueValidator(2022)],
        null=True,
        blank=False,
    )

    """metadta info field"""
    views = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    fav = models.ManyToManyField("users.user", related_name="fav_videoarts")
    today = models.BooleanField(default=False)
    like_it = models.IntegerField(
        default=0,
        blank=True,
    )

    """staff info field"""

    team = models.CharField(_("troupe"), max_length=300, null=True, blank=True)
    artist = models.CharField(_("regia"), max_length=300, null=True, blank=False)
    performer = models.CharField(_("performance"), max_length=300, null=True, blank=True)
    curator = models.CharField(_("curatori"),  max_length=300, null=True, blank=True)
    assistant_director = models.CharField(
        _("aiuto regia"), max_length=300, null=True, blank=True
    )
    screenwriter = models.CharField(_("sceneggiatura"), max_length=300, blank=True)
    casting = models.CharField(_("attori"), max_length=300, blank=True)
    editor = models.CharField(_("montaggio"), max_length=300, blank=True)
    director_of_photograpy = models.CharField(
        _("fotografia"), max_length=300, blank=True
    )
    audio_director = models.CharField(_("audio"), max_length=300, blank=True)
    phonic = models.CharField(_("fonico di presa diretta"), max_length=300, blank=True)
    edition_secretary = models.CharField(
        _("segretaria di edizione"), max_length=300, blank=True
    )
    music = models.CharField(_("musica"), max_length=300, blank=True)
    art_director = models.CharField(_("scenografia"), max_length=300, blank=True)
    costume_designer = models.CharField(_("costume"), max_length=300, blank=True)
    makeup_artist = models.CharField(_("trucco"), max_length=300, blank=True)
    spacial_effect_supervisor = models.CharField(
        _("effetti speciali"), max_length=300, blank=True
    )
    sound_designer = models.CharField(_("sound"), max_length=300, blank=True)
    animator = models.CharField(_("animazione"), max_length=300, blank=True)
    character_designer = models.CharField(
        _("character design"), max_length=300, blank=True
    )


    def __str__(self):
        return self.title

    def count_fav_users(self):
        fav_users = self.fav.all()
        num_fav_users = len(fav_users)

        return num_fav_users

    def formatted_duration(self):
        duration_sec = self.duration
        if duration_sec < 60 :
            duration = f"{duration_sec} sec"
            return duration
        else :
            duration = round(duration_sec / 60)
            return f"{duration} min"

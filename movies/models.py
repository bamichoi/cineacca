from django.db import models
from django.forms import widgets
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_model
from django.utils.translation import ugettext_lazy as _


class Movie(core_model.TimeStampedModel):

    """Movie Model Definition"""

    """video info field"""
    video = models.FileField(
        upload_to="movie_files",
        null=True,
        blank=False,
    )
    thumbnail = models.ImageField(
        _("thumbnail"),
        upload_to="movie_thumbnails",
        null=True,
        blank=False,
    )
    poster = models.ImageField(
        _("locandina"),
        upload_to="movie_posters",
        default="movie_posters/default_poster.png",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.user", related_name="movies", on_delete=models.CASCADE
    )
    duration = models.CharField(null=True, blank=True, max_length=300)
    title = models.CharField(_("titolo"), max_length=300, blank=False)
    description = models.TextField(_("sinossi"), max_length=1000, blank=False)
    year = models.IntegerField(
        _("anno"),
        validators=[MinValueValidator(1900), MaxValueValidator(2022)],
        null=True,
        blank=False,
    )
    views = models.IntegerField(default=0)

    """staff info field"""
    team = models.CharField(_("truppe"), max_length=300, null=True, blank=True)
    director = models.CharField(_("regia"), max_length=300, null=True, blank=False)
    screenwriter = models.CharField(_("sceneggiatura"), max_length=300, blank=True)
    casting = models.CharField(_("attori"), max_length=300, blank=True)
    editor = models.CharField(_("montaggio"), max_length=300, blank=True)
    director_of_photograpy = models.CharField(
        _("fotografia"), max_length=300, blank=True
    )
    audio_director = models.CharField(_("audio"), max_length=300, blank=True)
    music = models.CharField(_("musica"), max_length=300, blank=True)
    art_director = models.CharField(_("scenografia"), max_length=300, blank=True)
    costume_designer = models.CharField(_("costume"), max_length=300, blank=True)
    makeup_artist = models.CharField(_("make-up artist"), max_length=300, blank=True)
    spacial_effect_supervisor = models.CharField(
        _("effetto speciale"), max_length=300, blank=True
    )
    sound_designer = models.CharField(_("sound"), max_length=300, blank=True)
    rating = models.FloatField(default=0.0)
    fav = models.ManyToManyField("users.user", related_name="fav_movies")

    def __str__(self):
        return self.title

    def formatted(self):
        title = self.title if len(self.title) < 35 else f"{self.title[:35]}..."
        return {"title": title}

    def count_fav_users(self):
        fav_users = self.fav.all()
        num_fav_users = len(fav_users)

        return num_fav_users

from django.db import models
from django.forms import widgets
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_model
from django.utils.translation import ugettext_lazy as _


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
        default="movie_posters/default_poster.png",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.user", related_name="videoarts", on_delete=models.CASCADE
    )
    title = models.CharField(_("titolo"), max_length=300, blank=False)
    artist = models.CharField(_("artista"), max_length=300, null=True, blank=False)
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

    def __str__(self):
        return self.title

    def count_fav_users(self):
        fav_users = self.fav.all()
        num_fav_users = len(fav_users)

        return num_fav_users

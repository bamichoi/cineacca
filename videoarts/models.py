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
        blank=True,
    )  # seed 위해 임시로 null=True, Black=True
    thumbnail = models.ImageField(
        _("thumbnail"),
        upload_to="videoart_thumbnails",
        null=True,
        blank=True,  # seed 위해 임시로 null=True, Black=True
    )
    poster = models.ImageField(
        _("locandina"),
        upload_to="videoart_posters",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.user", related_name="videoarts", on_delete=models.CASCADE
    )
    duration = models.CharField(null=True, blank=True, max_length=300)
    title = models.CharField(_("titolo"), max_length=300)
    description = models.TextField(_("descrizione"), max_length=1000)
    year = models.IntegerField(
        _("anno"), validators=[MinValueValidator(1900)], null=True
    )
    views = models.IntegerField(default=0)

    """staff info field"""
    director = models.CharField(_("regia"), max_length=300, null=True)
    screenwriter = models.CharField(_("sceneggiatura"), max_length=300)
    casting = models.CharField(_("attori"), max_length=300)
    editor = models.CharField(_("montaggio"), max_length=300)
    director_of_photograpy = models.CharField(_("fotografia"), max_length=300)
    audio_director = models.CharField(_("audio"), max_length=300)
    music = models.CharField(_("musica"), max_length=300)
    art_director = models.CharField(_("scenografia"), max_length=300)
    costume_designer = models.CharField(_("costume"), max_length=300)
    makeup_artist = models.CharField(_("make-up artist"), max_length=300)
    spacial_effect_supervisor = models.CharField(_("effetto speciale"), max_length=300)
    sound_designer = models.CharField(_("sound"), max_length=300)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    def formatted(self):
        title = self.title if len(self.title) < 35 else f"{self.title[:35]}..."
        return {"title": title}

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
    user = models.ForeignKey(
        "users.user", related_name="videoarts", on_delete=models.CASCADE
    )
    duration = models.CharField(null=True, blank=True, max_length=300)
    title = models.CharField(_("titolo"), max_length=300)
    artist = models.CharField(_("artista"), max_length=300, null=True, blank=True)
    description = models.TextField(_("descrizione"), max_length=1000)
    year = models.IntegerField(
        _("anno"), validators=[MinValueValidator(1900)], null=True
    )
    views = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    def formatted(self):
        title = self.title if len(self.title) < 35 else f"{self.title[:35]}..."
        return {"title": title}

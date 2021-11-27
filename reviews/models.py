from django.db import models
from core import models as core_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Review(core_model.TimeStampedModel):

    """Review Model Definition"""

    user = models.ForeignKey(
        "users.user", related_name="reviews", on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        "movies.movie", related_name="reviews", on_delete=models.CASCADE
    )
    title = models.CharField(_("titolo"), max_length=300)
    content = models.TextField(_("testo"), max_length=1000)
    rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    fav = models.ManyToManyField("users.user", related_name="fav_reviews")
    like_it = models.IntegerField(
        default=0,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} - {self.movie}"

    def formatted(self):
        title = self.title if len(self.title) < 35 else f"{self.title[:35]}..."
        return {"title": title}

    def count_fav_users(self):
        fav_users = self.fav.all()
        num_fav_users = len(fav_users)
        return num_fav_users

    class Meta:
        ordering = ("-created",)


class VideoArtReview(core_model.TimeStampedModel):

    """Review Model Definition"""

    user = models.ForeignKey(
        "users.user", related_name="videoart_reviews", on_delete=models.CASCADE
    )
    videoart = models.ForeignKey(
        "videoarts.videoart", related_name="videoart_reviews", on_delete=models.CASCADE
    )
    title = models.CharField(_("titolo"), max_length=300)
    content = models.TextField(_("testo"))
    rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    fav = models.ManyToManyField("users.user", related_name="fav_videoart_reviews")
    like_it = models.IntegerField(
        default=0,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} - {self.videoart}"

    def formatted(self):
        title = self.title if len(self.title) < 35 else f"{self.title[:35]}..."
        return {"title": title}

    def count_fav_users(self):
        fav_users = self.fav.all()
        num_fav_users = len(fav_users)

        return num_fav_users

    class Meta:
        ordering = ("-created",)

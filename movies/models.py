from django.db import models
from django.urls import reverse
from core import models as core_model
from django.utils.translation import ugettext_lazy as _


class Movie(core_model.TimeStampedModel):

    """Movie Model Definition"""

    """video info field"""
    video = models.FileField(
        upload_to="movie_files", null=True, blank=True
    )  # seed 위해 임시로 null=True, Black=True
    thumnail = models.ImageField(
        _("locandina"),
        upload_to="movie_thumnails",
        null=True,
        blank=True,  # seed 위해 임시로 null=True, Black=True
    )
    user = models.ForeignKey(
        "users.user", related_name="movies", on_delete=models.CASCADE
    )
    title = models.CharField(_("titolo"), max_length=300)
    description = models.TextField(_("descrizione"), max_length=1000)
    views = models.IntegerField(default=0)

    """staff info field"""
    director = models.CharField(_("regista"), max_length=300, null=True)
    screenwriter = models.CharField(_("sceneggiatore"), max_length=300)
    casting = models.CharField(max_length=300)
    editor = models.CharField(_("montatore"), max_length=300)
    director_of_photograpy = models.CharField(_("fotografia"), max_length=300)
    audio_director = models.CharField(_("audio"), max_length=300)
    music = models.CharField(_("musica"), max_length=300)
    art_director = models.CharField(_("scenografia"), max_length=300)
    costume_designer = models.CharField(_("costume"), max_length=300)
    makeup_artist = models.CharField(_("make-up artista"), max_length=300)
    spacial_effect_supervisor = models.CharField(_("effetto speciale"), max_length=300)
    sound_designer = models.CharField(_("sound"), max_length=300)

    def __str__(self):
        return self.title

    def rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rate
                rating_avg = all_ratings / len(all_reviews)
            return "{0:.1f}".format(rating_avg)  # !) 반올림 없이 버리는 방법은..?
        else:
            return 0


# movies

## defualt data - movie info
### title
### year
### video file
### thumnail image
### description (drama)

## defualt data - staff info
### director
### screenwriter
### actors
### editor
### director of photograpy
### audio director
### music
### art director
### costume designer
### make-up artist
### special effect supervisor
### sound designer


## related data
### likes
### rate
### views

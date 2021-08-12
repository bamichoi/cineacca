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
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.title} - {self.movie}"

    class Meta:
        ordering = ("-created",)


# review

## default data
### writer (user)
### content
### rate

## related data
### movie
### likes


## add review comment?

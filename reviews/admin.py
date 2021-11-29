from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    list_display = ("__str__", "rate", "created")


@admin.register(models.VideoArtReview)
class VideoArtReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    list_display = ("__str__", "rate", "created")

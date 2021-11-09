from django import forms
from . import models


class MovieUploadForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = (
            "video",
            "thumnail",
            "title",
            "year",
            "description",
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

    def save(self, *args, **kwargs):
        movie = super().save(commit=False)
        return movie

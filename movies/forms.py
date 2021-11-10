from django import forms
from django.forms import widgets
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from . import models


class MovieUploadForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = (
            "video",
            "poster",
            "thumbnail",
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


class CustomClearableFileInput(ClearableFileInput):
    initial_text = _("attuale")
    input_text = _("nuovo")

    # !) text 없애도 : 이 안없어짐..
    # Overriding built-in widget templates 해야하는데 TempletesSetting


class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = (
            "video",
            "poster",
            "thumbnail",
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
        widgets = {
            "video": CustomClearableFileInput,
            "poster": CustomClearableFileInput,
            "thumnail": CustomClearableFileInput,
        }

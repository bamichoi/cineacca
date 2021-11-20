from django import forms
from django.forms import widgets
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from . import models


class VideoArtUploadForm(forms.ModelForm):
    class Meta:
        model = models.VideoArt
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
            "title": forms.TextInput(attrs={"placeholder": "Il titolo del video"}),
            "year": forms.TextInput(
                attrs={"placeholder": "l'anno in cui il video è uscito"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "una descrizione del video "}
            ),
            # charfield + choices 의 select field는 어떻게 placeholder를 달까. 아마도 accademia 모델이 하나 있어야할듯.
        }

    def save(self, *args, **kwargs):
        videoart = super().save(commit=False)
        return videoart


class CustomClearableFileInput(ClearableFileInput):
    initial_text = _("attuale")
    input_text = _("nuovo")

    # !) text 없애도 : 이 안없어짐..
    # Overriding built-in widget templates 해야하는데 TempletesSetting


class VideoArtUpdateForm(forms.ModelForm):
    class Meta:
        model = models.VideoArt
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


class DeleteVideoArtForm(forms.Form):

    agree = forms.BooleanField(
        required=False,
        label="Sì, ho capito. Sono d'accordo di eliminarlo",
        widget=forms.CheckboxInput,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Inserisci il tuo password"})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get("password")
        user = self.user
        if not user.check_password(password):
            raise forms.ValidationError("Il password non è corretto")

    def clean_agree(self):
        agree = self.cleaned_data.get("agree")
        if agree == False:
            raise forms.ValidationError("Non sei d'accordo dell'eliminazione")

from django import forms
from django.forms import widgets
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from . import models
from movies import forms as movie_forms


class VideoArtUploadForm(forms.ModelForm):
    class Meta:
        model = models.VideoArt
        fields = (
            "video",
            "thumbnail",
            "title",
            "year",
            "artist",
            "description",
        )
        widgets = {
            "video": forms.FileInput(attrs={"accept": "video/mp4"}),
            "title": forms.TextInput(attrs={"placeholder": "Il titolo del video"}),
            "year": forms.TextInput(
                attrs={"placeholder": "l'anno in cui il video è uscito"}
            ),
            "artist": forms.TextInput(attrs={"placeholder": "Il nome di artista"}),
            "description": forms.Textarea(
                attrs={"placeholder": "una descrizione del video "}
            ),
        }

    def save(self, *args, **kwargs):
        videoart = super().save(commit=False)
        return videoart


class VideoArtUpdateForm(forms.ModelForm):
    class Meta:
        model = models.VideoArt
        fields = (
            "video",
            "thumbnail",
            "title",
            "year",
            "artist",
            "description",
        )
        widgets = {
            "video": movie_forms.CustomClearableFileInput(
                attrs={"accept": "video/mp4"}
            ),
            "thumnail": movie_forms.CustomClearableFileInput,
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

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
            "team",
            "description",
            "director",
            "screenwriter",
            "casting",
            "director_of_photograpy",
            "editor",
            "audio_director",
            "phonic",
            "music",
            "art_director",
            "assistant_director",
            "edition_secretary",
            "costume_designer",
            "makeup_artist",
            "spacial_effect_supervisor",
            "sound_designer",
            "animator",
            "character_designer",
        )
        widgets = {
            "video": forms.FileInput(attrs={"accept": "video/mp4"}),
            "title": forms.TextInput(attrs={"placeholder": "Il titolo del film"}),
            "team": forms.TextInput(
                attrs={"placeholder": "Il nome della truppe (*opzionale)"}
            ),
            "year": forms.TextInput(
                attrs={"placeholder": "l'anno in cui il film è uscito"}
            ),
            "description": forms.Textarea(attrs={"placeholder": "i sinossi del film "}),
            # charfield + choices 의 select field는 어떻게 placeholder를 달까. 아마도 accademia 모델이 하나 있어야할듯.
            "director": forms.TextInput(
                attrs={"placeholder": "regista (*neccessario)"}
            ),
            "screenwriter": forms.TextInput(
                attrs={"placeholder": "sceneggiatore (*opzionale)"}
            ),
            "casting": forms.TextInput(
                attrs={"placeholder": "attori/attrice (*opzionale)"}
            ),
            "editor": forms.TextInput(attrs={"placeholder": "montatore (*opzionale)"}),
            "director_of_photograpy": forms.TextInput(
                attrs={"placeholder": "direttore della fotografia (*opzionale)"}
            ),
            "audio_director": forms.TextInput(
                attrs={"placeholder": "direttore dell'audio (*opzionale)"}
            ),
            "phonic": forms.TextInput(
                attrs={"placeholder": "fonico di presa diretta (*opzionale)"}
            ),
            "assistant_director": forms.TextInput(
                attrs={"placeholder": "aiuto regista (*opzionale)"}
            ),
            "edition_secretary": forms.TextInput(
                attrs={"placeholder": "segretaria di edizione (*opzionale)"}
            ),
            "music": forms.TextInput(attrs={"placeholder": "compositore (*opzionale)"}),
            "art_director": forms.TextInput(
                attrs={"placeholder": "scenografo (*opzionale)"}
            ),
            "costume_designer": forms.TextInput(
                attrs={"placeholder": "costumista (*opzionale)"}
            ),
            "makeup_artist": forms.TextInput(
                attrs={"placeholder": "truccatore (*opzionale)"}
            ),
            "spacial_effect_supervisor": forms.TextInput(
                attrs={"placeholder": "VFX artista (*opzionale)"}
            ),
            "sound_designer": forms.TextInput(
                attrs={"placeholder": "sound designer (*opzionale)"}
            ),
            "animator": forms.TextInput(
                attrs={"placeholder": "animatore (*opzionale)"}
            ),
            "character_designer": forms.TextInput(
                attrs={"placeholder": "character designer (*opzionale)"}
            ),
        }

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get('thumbnail')
        if thumbnail:
            if thumbnail.size > 10*1024*1024:
                raise forms.ValidationError("Thumnail si deve essere meno di 10MB")
            return thumbnail
        else:
            raise forms.ValidationError("Thumnail è necessario")

    
    def clean_poster(self):
        poster = self.cleaned_data.get('poster')
        if poster and (type(poster) != str):
            if poster.size > 10*1024*1024:
                raise forms.ValidationError("la locandia si deve essere meno di 10MB")
            return poster

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
            "team",
            "description",
            "director",
            "screenwriter",
            "casting",
            "director_of_photograpy",
            "editor",
            "audio_director",
            "phonic",
            "music",
            "art_director",
            "assistant_director",
            "edition_secretary",
            "costume_designer",
            "makeup_artist",
            "spacial_effect_supervisor",
            "sound_designer",
            "animator",
            "character_designer",
        )
        widgets = {
            "video": CustomClearableFileInput(attrs={"accept": "video/mp4"}),
            "poster": CustomClearableFileInput,
            "thumnail": CustomClearableFileInput,
        }

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get('thumbnail')
        if thumbnail:
            if thumbnail.size > 4*1024*1024:
                raise forms.ValidationError("Thumnail si deve essere meno di 10MB")
            return thumbnail

    
    def clean_poster(self):
        poster = self.cleaned_data.get('poster')
        if poster:
            if poster.size > 4*1024*1024:
                raise forms.ValidationError("La locandia si deve essere meno di 10MB")

class DeleteMovieForm(forms.Form):

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

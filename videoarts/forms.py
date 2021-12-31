from django import forms
from django.utils.translation import gettext_lazy as _
from . import models
from movies import forms as movie_forms
import subprocess
import http

class VideoArtUploadForm(forms.ModelForm):
    class Meta:
        model = models.VideoArt
        fields = (
            "video",
            "thumbnail",
            "poster",
            "title",
            "year",
            "description",
            "artist",
            "performer",
            "curator",
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
            "title": forms.TextInput(attrs={"placeholder": "Il titolo del video"}),
            "year": forms.TextInput(
                attrs={"placeholder": "l'anno in cui il video è uscito"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "una descrizione del video "}
            ),
            "artist": forms.TextInput(attrs={"placeholder": "regista (*neccessario)"}),
            "performer": forms.TextInput(attrs={"placeholder": "performer (*opzionale)"}),
            "curator": forms.TextInput(attrs={"placeholder": "curatore (*opzionale)"}),
            "artist": forms.TextInput(attrs={"placeholder": "regista (*neccessario)"}),
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
                raise forms.ValidationError("Cover image si deve essere meno di 10MB")
            return poster
    
    def clean_video(self):
        video = self.cleaned_data.get("video")
        if video:
            if video.size > 1500*1024*1024:
                raise forms.ValidationError("Il video si deve essre meno di 1.5GB")
            return video


    def save(self, *args, **kwargs):
        videoart = super().save(commit=False)
        video = self.cleaned_data.get("video")
        video_path = video.temporary_file_path()    
        get_duration =  subprocess.check_output(['ffprobe', '-i', f'{video_path}', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
        duration = int(float(get_duration.decode('utf-8').replace("\n", ""))) 
        videoart.duration = duration    
        return videoart


class VideoArtUpdateForm(forms.ModelForm):
    class Meta:
        model = models.VideoArt
        fields = (
            "video",
            "thumbnail",
            "poster",
            "title",
            "year",
            "description",
            "artist",
            "performer",
            "curator",
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
            "video": movie_forms.CustomClearableFileInput(
                attrs={"accept": "video/mp4"}
            ),
            "thumnail": movie_forms.CustomClearableFileInput,
            "poster": movie_forms.CustomClearableFileInput,
        }

    
    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get('thumbnail')
        if thumbnail:
            if thumbnail.size > 10*1024*1024:
                raise forms.ValidationError("Thumnail si deve essere meno di 10MB")
            return thumbnail

    
    def clean_poster(self):
        poster = self.cleaned_data.get('poster')
        if poster:
            if poster.size > 10*1024*1024:
                raise forms.ValidationError("Cover image si deve essere meno di 10MB")
            return poster
    
    def clean_video(self):
        video = self.cleaned_data.get("video")
        if video:
            if video.size > 1000*1024*1024:
                raise forms.ValidationError("Il video si deve essre meno di 1GB")
            return video

    def save(self, *args, **kwargs):

        videoart = super().save(commit=False)
        video = self.cleaned_data.get("video")
        try: 
            video_path = video.temporary_file_path()
            get_duration =  subprocess.check_output(['ffprobe', '-i', f'{video_path}', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
            duration = int(float(get_duration.decode('utf-8').replace("\n", ""))) 
            videoart.duration = duration
        except :
            pass

        super().save()
       

class DeleteVideoArtForm(forms.Form):

    agree = forms.BooleanField(
        required=False,
        label="Si, ho capito, procedi",
        widget=forms.CheckboxInput,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Inserisci la tua password"})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get("password")
        user = self.user
        if not user.check_password(password):
            raise forms.ValidationError("la password non è corretto")

    def clean_agree(self):
        agree = self.cleaned_data.get("agree")
        if agree == False:
            raise forms.ValidationError("Non hai acconsentito all'eliminazione")

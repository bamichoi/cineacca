from django import forms
from django.forms import widgets
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from . import models
from time import time
import subprocess

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
    
    
    def clean_video(self):
        video = self.cleaned_data.get("video")
        if video and (type(video) != str):
            if video.size > 500*1024*1024:
                raise forms.ValidationError("Il video si deve essre meno di 500MB")
            return video

    def save(self, *args, **kwargs):
        
        movie = super().save(commit=False)
        video = self.cleaned_data.get("video")
        video_path = video.temporary_file_path()
        get_duration =  subprocess.check_output(['ffprobe', '-i', f'{video_path}', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
        duration = int(float(get_duration.decode('utf-8').replace("\n", ""))) 
        movie.duration = duration

        """
        def clean_video(self):
            raw_video = self.cleaned_data.get("video")
            timestamp = int(time())
            raw_video_path = raw_video.temporary_file_path()
            video_name = f"{raw_video}".replace(" ", "_").split(".")[0]
            subprocess.run(f"ffmpeg -i {raw_video_path} -vcodec h264 -b:v 1000k -acodec mp3 -y uploads/movie_files/{video_name}_{timestamp}.mp4", shell=True)
            return f"movie_files/{video_name}_{timestamp}.mp4"
        """
       
         
        """
        movie.video = clean_video(self)
        video_path = movie.video.path
        get_duration =  subprocess.check_output(['ffprobe', '-i', f'{video_path}', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
        duration = int(float(get_duration.decode('utf-8').replace("\n", ""))) # 바로 int로 구하는 커맨드 라인이 있을 것이야. 
        movie.duration = duration
        """
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
            if thumbnail.size > 10*1024*1024:
                raise forms.ValidationError("Thumnail si deve essere meno di 10MB")
            return thumbnail

    
    def clean_poster(self):
        poster = self.cleaned_data.get('poster')
        if poster:
            if poster.size > 10*1024*1024:
                raise forms.ValidationError("La locandia si deve essere meno di 10MB")

    def clean_video(self):
        video = self.cleaned_data.get("video")
        if video and (type(video) != str):
            if video.size > 500*1024*1024:
                raise forms.ValidationError("Il video si deve essre meno di 500MB")
            return video

    def save(self, *args, **kwargs):
        
        movie = super().save(commit=False)
        video = self.cleaned_data.get("video")
        video_path = video.temporary_file_path()
        get_duration =  subprocess.check_output(['ffprobe', '-i', f'{video_path}', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
        duration = int(float(get_duration.decode('utf-8').replace("\n", ""))) 
        movie.duration = duration
        
        """
        def clean_video(self):
            raw_video = self.cleaned_data.get("video")
            timestamp = int(time())
            try:
                raw_video_path = raw_video.temporary_file_path()
                video_name = f"{raw_video}".split(".")[0]
                subprocess.run(f"ffmpeg -i {raw_video_path} -vcodec h264 -b:v 1000k -acodec mp3 -y uploads/movie_files/{video_name}_{timestamp}.mp4", shell=True)
                return f"movie_files/{video_name}_{timestamp}.mp4"
            except:
                return raw_video

        movie = super().save(commit=False)
        movie.video = clean_video(self)
        video_path = movie.video.path
        get_duration =  subprocess.check_output(['ffprobe', '-i', f'{video_path}', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
        duration = int(float(get_duration.decode('utf-8').replace("\n", ""))) # 바로 int로 구하는 커맨드 라인이 있을 것이야.
        movie.duration = duration
        """

        super().save()

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

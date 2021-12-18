from django import forms
from django.forms import widgets
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from pilkit.processors.resize import Thumbnail
from . import models
from movies import forms as movie_forms
from time import time
import subprocess

class VideoArtUploadForm(forms.ModelForm):
    class Meta:
        model = models.VideoArt
        fields = (
            "video",
            "thumbnail",
            "poster",
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

    def save(self, *args, **kwargs):

        def clean_video(self):
            raw_video = self.cleaned_data.get("video")
            timestamp = int(time())
            raw_video_path = raw_video.temporary_file_path()
            video_name = f"{raw_video}".split(".")[0]
            subprocess.run(f"ffmpeg -i {raw_video_path} -vcodec h264 -b:v 1000k -acodec mp3 -y uploads/videoart_files/{video_name}_{timestamp}.mp4", shell=True)
            return f"videoart_files/{video_name}_{timestamp}.mp4"

        videoart = super().save(commit=False)
        # 새로 업데이트 하는게 아닐 땐  작동 안하도록 해야함..
        videoart.video = clean_video(self)
        video_path = videoart.video.path
        get_duration =  subprocess.check_output(['ffprobe', '-i', f'{video_path}', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
        duration = int(float(get_duration.decode('utf-8').replace("\n", ""))) # 바로 int로 구하는 커맨드 라인이 있을 것이야. 
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
            "artist",
            "description",
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


    def save(self, *args, **kwargs):

        def clean_video(self):
            raw_video = self.cleaned_data.get("video")
            timestamp = int(time())
            try:
                raw_video_path = raw_video.temporary_file_path()
                video_name = f"{raw_video}".split(".")[0]
                subprocess.run(f"ffmpeg -i {raw_video_path} -vcodec h264 -b:v 1000k -acodec mp3 -y uploads/videoart_files/{video_name}_{timestamp}.mp4", shell=True)
                return f"videoart_files/{video_name}_{timestamp}.mp4"
            except:
                return raw_video

        videoart = super().save(commit=False)
        videoart.video = clean_video(self)
        video_path = videoart.video.path
        get_duration =  subprocess.check_output(['ffprobe', '-i', f'{video_path}', '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
        duration = int(float(get_duration.decode('utf-8').replace("\n", ""))) # 바로 int로 구하는 커맨드 라인이 있을 것이야.
        videoart.duration = duration
        super().save()

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

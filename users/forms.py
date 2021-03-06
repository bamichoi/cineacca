from django.forms import widgets
from django import forms
from django.contrib.auth.password_validation import validate_password
from movies import forms as movie_form
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import ugettext_lazy as _
from . import models


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "avatar", "sfondo", "school", "biography", "works")
        labels = {"works": "Lavori preferiti"}
        widgets = {
            "works": widgets.CheckboxSelectMultiple,
            "avatar": movie_form.CustomClearableFileInput,
            "sfondo": movie_form.CustomClearableFileInput,
        }


class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "ll tuo indrizzo email"}),
    )  # 각 필드 생성
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "la tua password"})
    )

    auto_login = forms.BooleanField(
        required=False,
        label="Auto login?",
        widget=forms.CheckboxInput()
    )

    def clean(self):  # email과 password는 서로 종속되어있다. 이 경우 clean method를 이용한다.
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)  # 해당 email의 user가 있는지 확인.
            if user.check_password(password):  # 있다면 check_password 로 password가 동일한지 확인.
                return self.cleaned_data  # 동일하다면 cleaned_data 리턴.
            else:
                self.add_error(
                    "password", forms.ValidationError("la password non è corretta.")
                )  # clean method 에서는 non field 에러를 띄우므로 add_error 로 특정
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("Quest'account non esiste."))


class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "school", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Il tuo nome"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Il tuo cognome"}),
            "school": forms.TextInput(
                attrs={"placeholder": "Il nome dell'istituto o team ecc."}
            ),
            "email": forms.TextInput(
                attrs={"placeholder": "l'indirizzo email per login"}
            ),
            # charfield + choices 의 select field는 어떻게 placeholder를 달까. 아마도 accademia 모델이 하나 있어야할듯.
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Inserisci la password"}),
        validators=[validate_password],
    )  # password 는 암호화되어 저장되어야 하므로 별도로 작성.
    password_confirm = forms.CharField(
        label="Verifica password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Inserisci ancora la password"}
        ),
    )

    def clean_password_confirm(self):  # password 와 password_confrim 이 일치하는지 확인.
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != None and password != password_confirm:
            raise forms.ValidationError("I due campi password non corrispondono.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.account_type = "student"
        user.set_password(password)
        user.save()


class PublicSignUpForm(forms.Form):

    first_name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={"placeholder": "Inserisci il tuo nome"}),
    )
    last_name = forms.CharField(
        label="Cognome",
        widget=forms.TextInput(attrs={"placeholder": "Inserisci il tuo cognome"}),
    )
    email = forms.EmailField(
        label="Indrizzo di email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Inserisci l'indirizzo email per login"}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Inserisci la password"}),
        validators=[validate_password],
    )  # password 는 암호화되어 저장되어야 하므로 별도로 작성.
    password_confirm = forms.CharField(
        label="Verifica password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Inserisci ancora la password"}
        ),
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "Utente con questo Indrizzo di email esiste già."
            )
        except models.User.DoesNotExist:
            return email

    def clean_password_confirm(self):  # password 와 password_confrim 이 일치하는지 확인.
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != None and password != password_confirm:
            raise forms.ValidationError("I due campi password non corrispondono.")
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = models.User.objects.create_user(email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.account_type = "public"
        user.save()


class DeleteAccountForm(forms.Form):

    agree = forms.BooleanField(
        required=False,
        label="Si, ho capito, voglio procedere.",
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
            raise forms.ValidationError("la password non è corretta")

    def clean_agree(self):
        agree = self.cleaned_data.get("agree")
        if agree == False:
            raise forms.ValidationError("Non hai acconsentito alla secessione")


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("Quest'account non esiste.")

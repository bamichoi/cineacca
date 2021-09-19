from config.settings import EMAIL_USE_TLS
from django import forms
from django.db.models import fields
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )  # 각 필드 생성
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
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
                    "password", forms.ValidationError("Password is wrong.")
                )  # clean method 에서는 non field 에러를 띄우므로 add_error 로 특정
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist."))


class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "school", "email")

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter the Password"})
    )  # password 는 암호화되어 저장되어야 하므로 별도로 작성.
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm the Password"})
    )

    def clean_password_confirm(self):  # password 와 password_confrim 이 일치하는지 확인.
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Password confirmation does not match.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.account_type = "student"
        user.set_password(password)
        user.save()


class PublicSignUpForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your emaill adress"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter the Password"})
    )  # password 는 암호화되어 저장되어야 하므로 별도로 작성.
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm the Password"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("This email already exists.")
        except models.User.DoesNotExist:
            return email

    def clean_password_confirm(self):  # password 와 password_confrim 이 일치하는지 확인.
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Password confirmation does not match.")
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

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get("password")
        print(password)
        user = self.user
        print(user)
        if not user.check_password(password):
            raise forms.ValidationError("Password doesn't match")

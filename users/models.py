import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail
from django.forms import widgets
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from pilkit.processors.base import Transpose
from pilkit.processors.resize import SmartResize
from core import models as core_models
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from config import settings


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users require an email field")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AbstractItem(core_models.TimeStampedModel):

    """Abstaract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Work(AbstractItem):

    """Work Model Definition"""


class User(AbstractUser):

    """User Model Definition"""

    ACCOUNT_TYPE_STUDENT = "student"
    ACCOUNT_TYPE_PUBLIC = "public"
    ACCOUNT_TYPE_CHOICES = (
        (ACCOUNT_TYPE_STUDENT, "Studente"),
        (ACCOUNT_TYPE_PUBLIC, "Pubblico"),
    )

    username = None  # email을 username으로 사용하기 위해 Abspython manage.py migratetractUser의 username을 none으로 override.

    first_name = models.CharField(_("Nome"), max_length=50, blank=False)
    last_name = models.CharField(_("Cognome"), max_length=50, blank=False)

    email = models.EmailField(
        _("Indrizzo di email"), unique=True
    )  # _ 는 ugettext_lazy()의 별칭. 언어설정에 따라 출력되는 문자열을 변환해주는 함수다.
    USERNAME_FIELD = "email"  # email을 username처럼 사용하기.
    REQUIRED_FIELDS = (
        []
    )  # AbsractUser에는 email이 Required로 잡혀있으나 USERNAME_FIELD로 사용되는 필드는 REQUIRED에 있으면 안된다.
    school = models.CharField(_("appartenuto a"), max_length=100, null=True, blank=True)
    avatar = ProcessedImageField(
        upload_to="user_avatars", 
        default="default_images/default_avatar.jpeg",
        processors=[Transpose(), ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 100}
    )
    biography = models.TextField(_("biografia"), null=True, blank=True)
    account_type = models.CharField(
        _("tipo d'account"),
        choices=ACCOUNT_TYPE_CHOICES,
        max_length=50,
        null=True,
        blank=True,
    )
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    works = models.ManyToManyField(
        "Work",
        related_name="users",
        blank=True,
    )
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.first_name = str.capitalize(self.first_name)
        self.last_name = str.capitalize(self.last_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("users:user_profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            if settings.DEBUG is True :
                domain = "http://127.0.0.1:8000"
            else :
                domain = "https://cineacca.herokuapp.com"
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret, "domain": domain}
            )
            send_mail(
                "Verificazione dell'account su CINEACCA",
                strip_tags(html_message),  # html을 제외한 부분을 text로 바꿔주는 기능.
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,  # 메일안에서 html 태그를 작동하게 함.
            )
            self.save()
        return


## necessary data
### email (ID) - email certification (only @abaroma.it accept)
### password
### full name
### school

## post-sign up data
### profile image
### bio

## related data
### Movies Uploaded
### likes
### review


# the public user

## necessary data
### email - email certification
### password
### full name

## post-sign up data
### profile image
### bio

## related data
### likes
### review

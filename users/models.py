from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


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


class User(AbstractUser):

    """User Model Definition"""

    SCHOOL_ACCA_ROMA = "acccademia_belle_arti_di_roma"
    SCHOOL_CHOICES = ((SCHOOL_ACCA_ROMA, "Accademia Belle Arti di Roma"),)

    ACCOUNT_TYPE_STUDENT = "student"
    ACCOUNT_TYPE_PUBLIC = "public"
    ACCOUNT_TYPE_CHOICES = (
        (ACCOUNT_TYPE_STUDENT, "Studente"),
        (ACCOUNT_TYPE_PUBLIC, "Publico"),
    )

    username = None  # email을 username으로 사용하기 위해 Abspython manage.py migratetractUser의 username을 none으로 override.

    email = models.EmailField(
        _("email address"), unique=True
    )  # _ 는 ugettext_lazy()의 별칭. 언어설정에 따라 출력되는 문자열을 변환해주는 함수다.
    USERNAME_FIELD = "email"  # email을 username처럼 사용하기.
    REQUIRED_FIELDS = (
        []
    )  # AbsractUser에는 email이 Required로 잡혀있으나 USERNAME_FIELD로 사용되는 필드는 REQUIRED에 있으면 안된다.
    school = models.CharField(
        _("accademia"), choices=SCHOOL_CHOICES, max_length=50, null=True, blank=True
    )
    avatar = models.ImageField(upload_to="user_avatars", null=True, blank=True)
    biography = models.TextField(_("biography"), null=True, blank=True)
    account_type = models.CharField(
        _("tipo d'account"),
        choices=ACCOUNT_TYPE_CHOICES,
        max_length=50,
        null=True,
        blank=True,
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.email


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

from django import forms
from django.forms import fields
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ("title", "rate", "content")

    def save(self, *args, **kwargs):
        review = super().save(commit=False)
        return review

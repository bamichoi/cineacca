from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from movies import models as movie_models
from reviews import models as review_models
from . import forms
from . import models


def create_review(request, pk):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        movie = movie_models.Movie.objects.get(pk=pk)
        if not movie:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect(reverse("movies:detail", kwargs={"pk": movie.pk}))


def delete_review(request, pk, review_pk):
    user = request.user
    try:
        review = review_models.Review.objects.get(pk=review_pk)
        if review.user.pk != user.pk:
            pass
        else:
            review.delete()
        return redirect(reverse("movies:detail", kwargs={"pk": pk}))
    except movie_models.Movie.DoesNotExist:
        redirect(reverse("core:home"))


def update_review(request):
    if request.method == "POST":
        pk = request.POST.get("pk")
        title = request.POST.get("title")
        rate = request.POST.get("rate")
        content = request.POST.get("content")
        review = models.Review.objects.get(
            pk=pk
        )  # !) filter 로 하면 왜 에러나지? : 'QuerySet' object has no attribute 'save'
        review.title = title
        review.rate = rate
        review.content = content
        review.save()

    return JsonResponse({"status": "Success"})

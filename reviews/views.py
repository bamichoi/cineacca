from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from movies import models as movie_models
from reviews import models as review_models
from . import forms
from . import models
from movies import models as movie_models


def create_review(request, pk):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        rate = request.POST.get("rate")
        content = request.POST.get("content")
        movie = movie_models.Movie.objects.get(pk=pk)
        review = models.Review.objects.create(
            user=user, title=title, rate=rate, content=content, movie=movie
        )
        return JsonResponse(
            {
                "title": review.title,
                "rate": review.rate,
                "content": review.content,
                "pk": review.pk,
            }
        )


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

    return JsonResponse({"status": "Success"})  # !) 이런식으로 JsonResponse 를 해줘야하는 이유?


def delete_review(request):
    if request.method == "POST":
        pk = request.POST.get("pk")
        review = models.Review.objects.get(pk=pk)
        review.delete()

    return JsonResponse({"status": "Success"})

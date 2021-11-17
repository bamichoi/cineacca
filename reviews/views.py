from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from movies import models as movie_models
from reviews import models as review_models
from . import forms
from . import models
from movies import models as movie_models


def get_rating(movie):
    all_reviews = movie.reviews.all()
    all_ratings = 0
    if len(all_reviews) > 0:
        for review in all_reviews:
            all_ratings += review.rate
            rating_avg = all_ratings / len(all_reviews)
        return float(
            "{0:.1f}".format(rating_avg)
        )  # !) 반올림 없이 버리는 방법은..? 이거 다시한번 봐야함 float없이.. string으로 나오면 안돼..
    else:
        return 0


# api 접근 따로 보호처리 해줘야하나?
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
        print(review.created)
        created = review.created.strftime("%d-%B-%Y-%H:%M")
        print(created)
        movie.rating = get_rating(movie)
        movie.save()
        return JsonResponse(
            {
                "title": review.title,
                "rate": review.rate,
                "content": review.content,
                "pk": review.pk,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "created": created,
            }
        )


def update_review(request):
    if request.method == "POST":
        pk = request.POST.get("pk")
        title = request.POST.get("title")
        rate = request.POST.get("rate")
        print(rate)
        content = request.POST.get("content")
        review = models.Review.objects.get(
            pk=pk
        )  # !) filter 로 하면 왜 에러나지? : 'QuerySet' object has no attribute 'save'
        review.title = title
        review.rate = rate
        review.content = content
        review.save()
        movie = review.movie
        movie.rating = get_rating(movie)
        movie.save()

    return JsonResponse({"status": "Success"})  # !) 이런식으로 JsonResponse 를 해줘야하는 이유?


def delete_review(request):
    if request.method == "POST":
        pk = request.POST.get("pk")
        review = models.Review.objects.get(pk=pk)
        movie = review.movie
        review.delete()
        movie.rating = get_rating(movie)
        movie.save()

    return JsonResponse({"status": "Success"})

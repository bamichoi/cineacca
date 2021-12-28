from typing import List
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from movies import models as movie_models
from reviews import models as review_models
from . import forms
from . import models
from movies import models as movie_models
from videoarts import models as videoart_models
import locale


class ReviewList(TemplateView):

    template_name = "reviews/review_list_total.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_reviews = models.Review.objects.all().order_by("-created")[:6]
        top_reviews = models.Review.objects.all().order_by("-like_it")[:6]
        new_videoart_reviews = models.VideoArtReview.objects.all().order_by("-created")[
            :6
        ]
        top_videoart_reviews = models.VideoArtReview.objects.all().order_by("-like_it")[
            :6
        ]

        context["new_reviews"] = new_reviews
        context["top_reviews"] = top_reviews
        context["new_videoart_reviews"] = new_videoart_reviews
        context["top_videoart_reviews"] = top_videoart_reviews

        return context


class MovieReviewList(ListView):

    model = models.Review
    paginate_by = 12
    context_object_name = "reviews"
    template_name = "reviews/review_list_movie.html"

    def get_context_data(
        self, **kwargs
    ):  # 현재 페이지에 따라 page 범위가 변하는 paginator 를 위해 get_context_data()로 context ovveride.
        sort = self.request.GET.get("sort_by")
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]  # ListView 에 내장된 paginator 들고 와주고
        page_numbers_range = 5  # 한번에 볼 수 있는 페이지 넘버 갯수.
        max_index = len(paginator.page_range)  # 총 페이지 갯수.
        page = self.request.GET.get("page")  # 현재 페이지의 넘버. page 파라미터 값 가져오기.

        # page값이 비어있을 경우의 예외처리. 만약 page 파라미터의 값을 current_page 의 값으로 설정. 없다면 항상 1page로 감.
        if page:
            current_page = int(page)
        else:
            current_page = 1

        start_index = (
            current_page - 3
        )  # 페이지 넘버 시작점 정하기. 현재 페이지 넘버 기준으로 항상 2페이지를 앞에서 시작.
        if start_index < 0:  # 만약 현재페이지가 3페이지와 같거나 그 앞이라면
            start_index = 0  # start_index는 0 을 가지고 previous 를 표시할지에 대한 조건문에 이용한다.

        end_index = (
            start_index + page_numbers_range
        )  # start_index에 한번에 볼 수 있는 페이지 넘버 갯수를 더해서 현재 표시하는 마지막 페이지 넘버를 정한다.
        if end_index >= max_index:  # 만약 마지막 페이지 넘버가 최대 페이지 넘버를 넘어가면
            end_index = max_index  # 마지막 페이지 넘버와 최대 페이지 넘버는 같다.

        page_range = paginator.page_range[start_index:end_index]  # 현재 렌더해야할 페이지 넘버들.

        """ 추후 순차적으로 넘어가는 paginator도 만들어보기 """
        # current_min_object_number = (max_index - current_page) * 20 + 1
        # object_number_range = range(current_min_object_number, 10)
        context["page_range"] = page_range
        context["current_page"] = current_page
        context["start_index"] = start_index
        context["next_index"] = end_index + 1
        context["max_index"] = max_index
        context["sort"] = sort
        # context["object_number_range"] = object_number_range

        return context


class VideoArtReviewList(ListView):

    model = models.VideoArtReview
    paginate_by = 12
    context_object_name = "reviews"
    template_name = "reviews/review_list_videoart.html"

    def get_context_data(
        self, **kwargs
    ):  # 현재 페이지에 따라 page 범위가 변하는 paginator 를 위해 get_context_data()로 context ovveride.
        sort = self.request.GET.get("sort_by")
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]  # ListView 에 내장된 paginator 들고 와주고
        page_numbers_range = 5  # 한번에 볼 수 있는 페이지 넘버 갯수.
        max_index = len(paginator.page_range)  # 총 페이지 갯수.
        page = self.request.GET.get("page")  # 현재 페이지의 넘버. page 파라미터 값 가져오기.

        # page값이 비어있을 경우의 예외처리. 만약 page 파라미터의 값을 current_page 의 값으로 설정. 없다면 항상 1page로 감.
        if page:
            current_page = int(page)
        else:
            current_page = 1

        start_index = (
            current_page - 3
        )  # 페이지 넘버 시작점 정하기. 현재 페이지 넘버 기준으로 항상 2페이지를 앞에서 시작.
        if start_index < 0:  # 만약 현재페이지가 3페이지와 같거나 그 앞이라면
            start_index = 0  # start_index는 0 을 가지고 previous 를 표시할지에 대한 조건문에 이용한다.

        end_index = (
            start_index + page_numbers_range
        )  # start_index에 한번에 볼 수 있는 페이지 넘버 갯수를 더해서 현재 표시하는 마지막 페이지 넘버를 정한다.
        if end_index >= max_index:  # 만약 마지막 페이지 넘버가 최대 페이지 넘버를 넘어가면
            end_index = max_index  # 마지막 페이지 넘버와 최대 페이지 넘버는 같다.

        page_range = paginator.page_range[start_index:end_index]  # 현재 렌더해야할 페이지 넘버들.

        """ 추후 순차적으로 넘어가는 paginator도 만들어보기 """
        # current_min_object_number = (max_index - current_page) * 20 + 1
        # object_number_range = range(current_min_object_number, 10)
        context["page_range"] = page_range
        context["current_page"] = current_page
        context["start_index"] = start_index
        context["next_index"] = end_index + 1
        context["max_index"] = max_index
        context["sort"] = sort
        # context["object_number_range"] = object_number_range

        return context


class MovieReviewDetail(DetailView):
    model = models.Review
    template_name = "reviews/review_detail_movie.html"
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            fav_reviews = user.fav_reviews.all()
            context["fav_reviews"] = fav_reviews

        return context


class VideoArtReviewDetail(DetailView):
    model = models.VideoArtReview
    template_name = "reviews/review_detail_videoart.html"
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            fav_reviews = user.fav_videoart_reviews.all()
            context["fav_reviews"] = fav_reviews

        return context


def get_rating(video, type):
    if type == "movie":
        all_reviews = video.reviews.all()
    else:
        all_reviews = video.videoart_reviews.all()
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
        object_type = request.POST.get("object_type")

        if object_type == "movie":
            movie = movie_models.Movie.objects.get(pk=pk)
            review = models.Review.objects.create(
                user=user, title=title, rate=rate, content=content, movie=movie
            )
            locale.setlocale(locale.LC_ALL, "it_IT.UTF-8") # !) 이 부분 잘 이해 못했다.
            created = review.created.now().strftime("%d-%B-%Y-%H:%M") # localse.setlocale 없이 그대로 넘겨주면 utc0 시간으로 나온다.
            movie.rating = get_rating(movie, "movie")
            movie.save()
        else:
            videoart = videoart_models.VideoArt.objects.get(pk=pk)
            review = models.VideoArtReview.objects.create(
                user=user, title=title, rate=rate, content=content, videoart=videoart
            )
            locale.setlocale(locale.LC_ALL, "it_IT.UTF-8")
            created = review.created.strftime("%d-%B-%Y-%H:%M")
            videoart.rating = get_rating(videoart, "videoart")
            videoart.save()
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
        content = request.POST.get("content")
        object_type = request.POST.get("object_type")

        if object_type == "movie":
            review = models.Review.objects.get(
                pk=pk
            )  # !) filter 로 하면 왜 에러나지? : 'QuerySet' object has no attribute 'save'
            review.title = title
            review.rate = rate
            review.content = content
            review.save()
            movie = review.movie
            movie.rating = get_rating(movie, "movie")
            movie.save()
        else:
            review = models.VideoArtReview.objects.get(pk=pk)
            review.title = title
            review.rate = rate
            review.content = content
            review.save()
            videoart = review.videoart
            videoart.rating = get_rating(videoart, "videoart")
            videoart.save()

    return JsonResponse({"status": "Success"})  # !) 이런식으로 JsonResponse 를 해줘야하는 이유?


def delete_review(request):
    if request.method == "POST":
        pk = request.POST.get("pk")
        object_type = request.POST.get("object_type")

        if object_type == "movie":
            review = models.Review.objects.get(pk=pk)
            movie = review.movie
            review.delete()
            movie.rating = get_rating(movie, "movie")
            movie.save()
        else:
            review = models.VideoArtReview.objects.get(pk=pk)
            videoart = review.videoart
            review.delete()
            videoart.rating = get_rating(videoart, "videoart")
            videoart.save()

    return JsonResponse({"status": "Success"})


def switch_fav_view(request, pk):
    if request.method == "POST":
        handleType = request.POST.get("handleType")
        objType = request.POST.get("objType")
        user = request.user
        if objType == "movie":
            review = models.Review.objects.get(pk=pk)
        else:
            review = models.VideoArtReview.objects.get(pk=pk)

        if handleType == "add":
            try:
                review.fav.add(user)
                review.like_it += 1
                review.save()
                num_fav_users = review.count_fav_users()
                return JsonResponse({"result": "added", "numFavUsers": num_fav_users})
            except:
                return redirect("core:home")
        else:
            try:
                review.fav.remove(user)
                review.like_it -= 1
                review.save()
                num_fav_users = review.count_fav_users()
                return JsonResponse({"result": "removed", "numFavUsers": num_fav_users})
            except:
                return redirect("core:home")

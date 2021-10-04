from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import (
    ListView,
    DetailView,
    View,
    FormView,
    UpdateView,
    DeleteView,
)
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from reviews import forms as review_form
from . import models
from . import forms
from users import mixins as user_mixins

# Create your views here.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Movie
    paginate_by = 12
    ordering = "-created"
    context_object_name = "movies"
    template_name = "home.html"


class MovieUpload(user_mixins.MoiveUploadPermissionView, FormView):

    """MovieUpload View Definition"""

    form_class = forms.MovieUploadForm
    template_name = "movies/movie_upload.html"

    def form_valid(self, form):
        movie = form.save()
        movie.user = self.request.user
        movie.save()
        return redirect(reverse("movies:detail", kwargs={"pk": movie.pk}))


class UpdateMovie(user_mixins.MovieUpdateDeletePermissionView, UpdateView):

    """UpdateMovie View Deifinitiom"""

    template_name = "movies/movie_update.html"
    model = models.Movie

    fields = (
        "video",
        "thumnail",
        "title",
        "description",
        "director",
        "screenwriter",
        "casting",
        "editor",
        "director_of_photograpy",
        "audio_director",
        "music",
        "art_director",
        "costume_designer",
        "makeup_artist",
        "spacial_effect_supervisor",
        "sound_designer",
    )

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("movies:detail", kwargs={"pk": pk})


class DeleteMovie(user_mixins.MovieUpdateDeletePermissionView, DeleteView):

    model = models.Movie
    template_name = "movies/movie_delete.html"
    success_url = reverse_lazy("movies:list")


class MovieList(ListView):

    """MovieList Definition"""

    model = models.Movie
    paginate_by = 24
    ordering = "-created"
    context_object_name = "movies"

    def get_context_data(
        self, **kwargs
    ):  # 현재 페이지에 따라 page 범위가 변하는 paginator 를 위해 get_context_data()로 context ovveride.
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
        # context["object_number_range"] = object_number_range

        return context


class MovieDetail(DetailView):

    """MovieDetail Definition"""

    model = models.Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()
        all_reviews = movie.reviews.all()
        page = self.request.GET.get("page", 1)
        page_numbers_range = 5
        paginator = Paginator(all_reviews, page_numbers_range)
        reviews = paginator.get_page(int(page))  # !) page, get_page 차이에 대해서..(맨날 까먹음)
        max_index = paginator.num_pages

        if page:
            current_page = int(page)
        else:
            current_page = 1

        start_index = current_page - 3
        if start_index < 0:
            start_index = 0

        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]

        context["reviews"] = reviews
        context["page_range"] = page_range
        context["start_index"] = start_index
        context["next_index"] = end_index + 1
        context["max_index"] = max_index

        return context


class SearchView(View):
    """SearchView Definition"""

    def get(self, request):

        keyword = self.request.GET.get("keyword")  # url에서 keyword 파라미터 값 들고오기.

        if keyword:  # keyword 값이 비어있지 않다면

            result_qs = models.Movie.objects.filter(
                Q(title__contains=keyword) | Q(director__contains=keyword)
            ).order_by(
                "-created"
            )  # keyword와 일치하는 오브젝트들의 쿼리셋 만들기.

            # paginator 생성
            page_numbers_range = 10
            paginator = Paginator(result_qs, page_numbers_range)
            page = self.request.GET.get("page", 1)
            max_index = paginator.num_pages
            movies = paginator.get_page(page)

            if page:
                current_page = int(page)
            else:
                current_page = 1

            start_index = current_page - 3
            if start_index < 0:
                start_index = 0

            end_index = start_index + page_numbers_range
            if end_index >= max_index:
                end_index = max_index

            page_range = paginator.page_range[start_index:end_index]

            return render(
                request,
                "movies/movie_search.html",
                {
                    "movies": movies,
                    "keyword": keyword,
                    "page_range": page_range,
                    "start_index": start_index,
                    "end_index": end_index,
                    "max_index": max_index,
                },
            )
        else:
            return render(
                request,
                "movies/movie_search.html",
                {"keyword": keyword, "start_index": 0},
            )


def count_view(request, pk):
    if request.method == "POST":
        try:
            movie = models.Movie.objects.get(pk=pk)
            movie.views += 1
            movie.save()
            return JsonResponse({"status": "Success"})
        except models.Movie.DoesNotExist:
            return redirect("core:home")

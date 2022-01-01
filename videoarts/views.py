from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    View,
    FormView,
    UpdateView,
)
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Q
from . import models
from . import forms
from users import mixins as user_mixins

class VideoArtUpload(user_mixins.MoiveUploadPermissionView, FormView):

    """VideoartUpload View Definition"""

    form_class = forms.VideoArtUploadForm
    template_name = "videoarts/videoart_upload.html"

    def form_valid(self, form):
        videoart = form.save()
        videoart.user = self.request.user
        videoart.save()
        return redirect(reverse("videoarts:detail", kwargs={"pk": videoart.pk}))



class UpdateVideoArt(user_mixins.VideoArtUpdateDeletePermissionView, UpdateView):

    """UpdateVideoArt View Deifinitiom"""

    template_name = "videoarts/videoart_update.html"
    model = models.VideoArt
    form_class = forms.VideoArtUpdateForm


    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("videoarts:detail", kwargs={"pk": pk})

    

class VideoArtList(ListView):

    """VideoArtList Definition"""

    model = models.VideoArt
    paginate_by = 15
    context_object_name = "videoarts"
    template_name = "videoarts/videoarts_list.html"

    def get_ordering(self):
        ordering = super().get_ordering()
        sort_by = self.request.GET.get("sort_by")
        if sort_by == "views":
            ordering = "-views"
        elif sort_by == "date":
            ordering = "-created"
        elif sort_by == "rating":
            ordering = "-rating"
        elif sort_by == "love":
            ordering = "-like_it"
        else:
            ordering = "-created"

        return ordering

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


class VideoArtDetail(DetailView):

    """VideoArtDetail Definition"""

    model = models.VideoArt

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videoart = self.get_object()
        user = self.request.user
        all_reviews = videoart.videoart_reviews.all()
        num_reviews = len(all_reviews)
        show_reviews = all_reviews[0:10]
        hidden_reviews = all_reviews[11:]
        num_hidden_reviews = len(hidden_reviews)

        num_fav_users = len(videoart.fav.all())

        try:  # !) Review Detail 처럼 user.authenticated 사용하면 더 간단. template에도 fav_exists 필요없이 in 사용해서 체크가능.
            fav_videoarts = user.fav_videoarts.all()
            fav_reviews = user.fav_videoart_reviews.all()
            if videoart in fav_videoarts:
                fav_exists = True
            else:
                fav_exists = False
            context["fav_exists"] = fav_exists
            context["fav_reviews"] = fav_reviews
        except:
            pass

        context["show_reviews"] = show_reviews
        context["hidden_reviews"] = hidden_reviews
        context["num_hidden_reviews"] = num_hidden_reviews
        context["num_reviews"] = num_reviews
        context["num_fav_users"] = num_fav_users

        return context


def switch_fav_view(request, pk):
    if request.method == "POST":
        handleType = request.POST.get("handleType")  # type은 예약어.
        user = request.user
        videoart = models.VideoArt.objects.get(pk=pk)
        if handleType == "add":
            try:
                videoart.fav.add(user)
                videoart.like_it += 1
                videoart.save()
                return JsonResponse({"result": "added"})
            except models.VideoArt.DoesNotExist:
                return redirect("core:home")
        else:
            try:
                videoart.fav.remove(user)
                videoart.like_it -= 1
                videoart.save()
                return JsonResponse({"result": "removed"})
            except models.VideoArt.DoesNotExist:
                return redirect("core:home")


@login_required(login_url="/users/login/")
def delete_videoart(request, pk):
    videoarts = models.VideoArt.objects.get(pk=pk)
    user = request.user

    if user == videoarts.user:

        if request.method == "POST":
            form = forms.DeleteVideoArtForm(
                request.user, request.POST
            )  # !) request.POST 넣어줘야하는 이유..?

            if form.is_valid():
                videoarts.delete()
                return redirect(reverse("core:home"))
        else:
            form = forms.DeleteVideoArtForm(request.user)

        return render(request, "videoarts/videoart_delete.html", {"form": form})

    else:
        return redirect("videoarts:list")


class SearchView(View):
    """SearchView Definition"""

    def get(self, request):

        keyword = self.request.GET.get("keyword")  # url에서 keyword 파라미터 값 들고오기.
        sort = self.request.GET.get("sort_by")

        if keyword:  # keyword 값이 비어있지 않다면

            result_qs = models.VideoArt.objects.filter(
                Q(title__contains=keyword)
                | Q(user__last_name__contains=keyword)
                | Q(user__first_name__contains=keyword)
            ).order_by(
                "-created"
            )  # keyword와 일치하는 오브젝트들의 쿼리셋 만들기.

            if sort:
                if sort == "views":
                    result_qs = result_qs.order_by("-views")
                elif sort == "date":
                    result_qs = result_qs.order_by("-created")
                elif sort == "rating":
                    result_qs = result_qs.order_by("-rating")
                elif sort == "love":
                    result_qs = result_qs.order_by("-like_it")

            # paginator 생성
            page_numbers_range = 15
            paginator = Paginator(result_qs, page_numbers_range)
            page = self.request.GET.get("page", 1)
            max_index = paginator.num_pages
            videoarts = paginator.get_page(page)

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
                "videoarts/videoart_search.html",
                {
                    "videoarts": videoarts,
                    "keyword": keyword,
                    "page_range": page_range,
                    "start_index": start_index,
                    "current_page": current_page,
                    "end_index": end_index,
                    "max_index": max_index,
                    "sort": sort,
                },
            )
        else:
            return render(
                request,
                "videoarts/videoart_search.html",
                {"start_index": 0},
            )


def count_view(request, pk):
    if request.method == "POST":
        try:
            videoarts = models.VideoArt.objects.get(pk=pk)
            videoarts.views += 1
            videoarts.save()
            return JsonResponse({"status": "Success"})
        except models.VideoArt.DoesNotExist:
            return redirect("core:home")

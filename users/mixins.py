from users.models import User
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from movies import models as movie_models
from videoarts import models as videoart_models


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")


class EmailLoginOnlyView(UserPassesTestMixin):
    pass  # Todo: 구글 연동 로그인 구현 뒤 작성하기.


# LoginRequireMixin과 UserPassesTestMixin 을 같이 동시에 사용할 수 있는지 재확인 필요.
class MoiveUploadPermissionView(UserPassesTestMixin):
    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        return (
            self.request.user.email_verified
            and self.request.user.account_type == "student"
        )

    def handle_no_permission(self):
        if (
            self.request.user.is_authenticated
            and self.request.user.account_type == "student"
        ):
            return render(self.request, "emails/request_verify.html")
        return redirect("core:home")  # 퍼블릭으로 로그인 되어있을때 student account 전용 알림 페이지를 만들까?


class MovieUpdateDeletePermissionView(UserPassesTestMixin):
    def test_func(self):
        movie_pk = self.kwargs.get("pk")
        try:
            movie = movie_models.Movie.objects.get(pk=movie_pk)
            return (
                self.request.user.is_authenticated and movie.user == self.request.user
            )
        except movie_models.Movie.DoesNotExist:
            return False

    def handle_no_permission(self):
        return redirect("core:home")


class VideoArtUpdateDeletePermissionView(UserPassesTestMixin):
    def test_func(self):
        videoart_pk = self.kwargs.get("pk")
        try:
            videoart = videoart_models.VideoArt.objects.get(pk=videoart_pk)
            return (
                self.request.user.is_authenticated
                and videoart.user == self.request.user
            )
        except videoart_models.VideoArt.DoesNotExist:
            return False

    def handle_no_permission(self):
        return redirect("core:home")


""" !) Mixin을 공유하기 위해 url 에서 videoart/movie 를 str prameter 값으로 이용해서 분기를 해주었지만 링크된 url을 잃어버림..
class MovieUpdateDeletePermissionView(UserPassesTestMixin):
    def test_func(self):
        obj_type = self.kwargs.get("obj_type")

        if obj_type == "movies":
            movie_pk = self.kwargs.get("pk")
            try:
                movie = movie_models.Movie.objects.get(pk=movie_pk)
                return (
                    self.request.user.is_authenticated
                    and movie.user == self.request.user
                )
            except movie_models.Movie.DoesNotExist:
                return False
        else:
            videoart_pk = self.kwargs.get("pk")
            try:
                videoart = videoart_models.VideoArt.objects.get(pk=videoart_pk)
                return (
                    self.request.user.is_authenticated
                    and videoart.user == self.request.user
                )
            except videoart_models.VideoArt.DoesNotExist:
                return False

    def handle_no_permission(self):
        return redirect("core:home")
"""

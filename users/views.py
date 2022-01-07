import os
import json
from django.views.generic.base import TemplateView
import requests
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.views.generic import (
    ListView,
    DetailView,
    View,
    FormView,
    UpdateView,
)
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages
from . import models, forms, mixins
from config import settings
# Create your views here.


class UserDashBoardList(ListView):

    template_name = "dashboards/user_dashboard_list.html"
    ordering = "-created"

    def get_queryset(self):
        pk = self.kwargs["pk"]
        list_by = self.kwargs["list_by"]
        user_obj = models.User.objects.get(pk=pk)

        if list_by == "movie":
            qs = user_obj.movies.all().order_by("-created")
        elif list_by == "videoart":
            qs = user_obj.videoarts.all().order_by("-created")
        elif list_by == "movie_review":
            qs = user_obj.reviews.all().order_by("-created")
        elif list_by == "videoart_review":
            qs = user_obj.videoart_reviews.all().order_by("-created")
        elif list_by == "fav_movie":
            qs = reversed(user_obj.fav_movies.all())
        elif list_by == "fav_videoart":
            qs = reversed(user_obj.fav_videoarts.all())
        elif list_by == "fav_review":
            qs = reversed(user_obj.fav_reviews.all())
        elif list_by == "fav_videoart_review":
            qs = reversed(user_obj.fav_videoart_reviews.all())

        return qs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        user_obj = models.User.objects.get(pk=pk)
        list_by = self.kwargs["list_by"]
        qs = self.get_queryset()

        if list_by == "movie" or list_by == "fav_movie":
            route_url = "movies:detail"
        elif list_by == "videoart" or list_by == "fav_videoart":
            route_url = "videoarts:detail"
        elif list_by == "movie_review" or list_by == "fav_review":
            route_url = "reviews:detail-movie"
        elif list_by == "videoart_review" or list_by == "fav_videoart_review":
            route_url = "reviews:detail-videoart"

        context["user_obj"] = user_obj
        context["list_by"] = list_by
        context["qs"] = qs
        context["route_url"] = route_url

        return context


class UserDashBoardView(TemplateView):
    template_name = "dashboards/user_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        user_obj = models.User.objects.get(pk=pk)

        movies_uploaded = user_obj.movies.all().order_by("-created")[:3]
        videoarts_uploaded = user_obj.videoarts.all().order_by("-created")[:3]
        movie_reviews_uploaded = user_obj.reviews.all().order_by("-created")[:3]
        videoart_reviews_uploaded = user_obj.videoart_reviews.all().order_by(
            "-created"
        )[:3]

        movies_loved = user_obj.fav_movies.all()[::-1][:3]
        videoarts_loved = user_obj.fav_videoarts.all()[::-1][:3]
        movie_reviews_loved = user_obj.fav_reviews.all()[::-1][:3]
        videoart_reviews_loved = user_obj.fav_videoart_reviews.all()[::-1][:3]

        context["user_obj"] = user_obj
        context["movies_uploaded"] = movies_uploaded
        context["videoarts_uploaded"] = videoarts_uploaded
        context["movie_reviews_uploaded"] = movie_reviews_uploaded
        context["videoart_reviews_uploaded"] = videoart_reviews_uploaded
        context["movies_loved"] = movies_loved
        context["videoarts_loved"] = videoarts_loved
        context["movie_reviews_loved"] = movie_reviews_loved
        context["videoart_reviews_loved"] = videoart_reviews_loved

        return context


class UserProfileView(DetailView):

    """UserProfile Definition"""

    model = models.User
    template_name = "users/user_profile.html"
    context_object_name = "user_obj"


class UpdateProfileView(mixins.LoggedInOnlyView, UpdateView):

    """ChangeProfile View Definition"""

    model = models.User
    form_class = forms.UpdateProfileForm
    template_name = "users/update-profile.html"

    def get_object(self, queryset=None):
        return self.request.user


class ChangePasswordView(mixins.LoggedInOnlyView, PasswordChangeView):

    """PasswordChange View Definition"""

    # !) Form 을 따로 사용하는게 더 좋을까나?

    template_name = "users/change-password.html"
    success_url = reverse_lazy("core:home") # 비번 변경후 성공메세지 띄우고 로그아웃 다시 로그인하게 하기

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["old_password"].label = "Password attuale"
        form.fields["old_password"].widget.attrs = {
            "placeholder": "Inserisci la tua password attuale"
        }
        form.fields["new_password1"].label = "Nuova password"
        form.fields["new_password1"].widget.attrs = {
            "placeholder": "Inserisci la nuova password"
        }
        form.fields["new_password2"].label = "Conferma nuova password"
        form.fields["new_password2"].widget.attrs = {
            "placeholder": "Inserisci ancora la nuova password"
        }
        return form


class StudentListView(ListView):

    """StudentList View Definition"""

    model = models.User
    paginate_by = 21
    context_object_name = "students"
    template_name = "users/student_list.html"

    def get_queryset(self):
        filter_by = self.request.GET.get("filter_by")
        sort_by = self.request.GET.get("sort_by")

        qs = super().get_queryset().filter(account_type="student").order_by("?")

        if filter_by != "None" and filter_by is not None:
            qs = qs.filter(works=filter_by).order_by("?")

        if sort_by == "az":
            qs = qs.order_by("last_name")
        elif sort_by == "za":
            qs = qs.order_by("-last_name")

        return qs

    def get_context_data(
        self, **kwargs
    ):  # 현재 페이지에 따라 page 범위가 변하는 paginator 를 위해 get_context_data()로 context ovveride.
        filter_by = self.request.GET.get("filter_by")
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
        context["start_index"] = start_index
        context["next_index"] = end_index + 1
        context["max_index"] = max_index
        context["current_page"] = current_page
        context["sort"] = sort
        context["filter_by"] = filter_by
        # context["object_number_range"] = object_number_range

        return context


class SearchView(View):

    """Search View Definition"""

    def get(self, request):

        keyword = self.request.GET.get("keyword")  # url에서 keyword 파라미터 값 들고오기.
        filter_by = self.request.GET.get("filter_by")
        sort = self.request.GET.get("sort_by")

        if keyword:  # keyword 값이 비어있지 않다면
            result_qs = models.User.objects.filter(account_type="student").filter(
                Q(first_name__contains=keyword) | Q(last_name__contains=keyword)
            ).order_by(
                "-date_joined"
            )  # keyword와 일치하는 오브젝트들의 쿼리셋 만들기.

            if filter_by != "None" and filter_by is not None:
                result_qs = result_qs.filter(works=filter_by).order_by("?")

            if sort == "az":
                result_qs = result_qs.order_by("last_name")
            elif sort == "za":
                result_qs = result_qs.order_by("-last_name")

            # paginator 생성
            page_numbers_range = 12
            paginator = Paginator(result_qs, page_numbers_range)
            page = self.request.GET.get("page", 1)
            max_index = paginator.num_pages
            students = paginator.get_page(page)

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
                "users/student_search.html",
                {
                    "students": students,
                    "keyword": keyword,
                    "page_range": page_range,
                    "start_index": start_index,
                    "end_index": end_index,
                    "max_index": max_index,
                    "sort": sort,
                    "filter_by": filter_by,
                    "current_page": current_page,
                },
            )
        else:
            return render(
                request,
                "users/user_search.html",
                {"keyword": keyword, "start_index": 0},
            )


class LoginView(mixins.LoggedOutOnlyView, FormView):

    """LoginView Definition"""

    template_name = "users/login.html"
    form_class = forms.LoginForm
    # success_url = reverse_lazy("core:home")  # !)reverse_lazy 와 reverse 의 차이?

    def form_valid(self, form):
        email = form.cleaned_data.get("email")  # form으로부터 clean된 email data를 받아옴.
        password = form.cleaned_data.get(
            "password"
        )  # form으로부터 clean된 password data를 받아옴.
        auto_login = form.cleaned_data.get("auto_login")
        user = authenticate(
            self.request, username=email, password=password
        )  # login 인증 부분
        if user is not None:
            login(self.request, user)  # login 시키기
            if auto_login == False:
                self.request.session.set_expiry(0)
            messages.info(self.request, f"Ciao, {user.first_name}!")
        return super().form_valid(form)  # 최종적으로 form_valid 가 유효하다면 succes_url로 넘겨주기

    def get_success_url(self):  # mixin 활용을 위해 success_url 대신 get_success_url 작성.
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def log_out(request):  # logout은 fbv로만 가능.
    logout(request)
    messages.info(request, f"Bye, See you!")
    return redirect(reverse("users:login"))


def sign_up(request):
    return render(request, "users/signup.html")


class StudentSignupView(mixins.LoggedOutOnlyView, FormView):

    """StudentSignupView Definition"""

    template_name = "users/student_signup.html"
    form_class = forms.StudentSignUpForm
    success_url = reverse_lazy("users:signup_success")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            user.verify_email()
        return super().form_valid(form)


class PublicSignupView(mixins.LoggedOutOnlyView, FormView):

    """StudentSignupView Definition"""

    template_name = "users/public_signup.html"
    form_class = forms.PublicSignUpForm
    success_url = reverse_lazy("users:signup_success")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            user.verify_email()
        return super().form_valid(form)


def signup_success(request):
    user = request.user
    user_email = user.email
    return render(request, "emails/signup_success.html", {"email": user_email})


def user_verified(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        messages.success(request, f"Il tuo account è verificato!")
    except models.User.DoesNotExist:
        # 에러메세지
        pass
    return redirect(reverse("core:home"))


def send_verify_email(request, pk):
    if request.user.is_authenticated:
        try:
            profile_user = models.User.objects.get(pk=pk)
            if profile_user == request.user:
                user_email = profile_user.email
                profile_user.verify_email()
                return render(
                    request, "emails/send_success.html", {"email": user_email}
                )
            else:
                pass
        except models.User.DoesNotExist:
            pass
    return redirect(reverse("core:home"))


class ResetPasswordView(PasswordResetView):
    template_name = "users/reset-password.html"
    from_email = settings.EMAIL_FROM
    success_url = reverse_lazy("users:reset-password-done")
    email_template_name = "emails/reset-password-email.html"
    html_email_template_name = "emails/reset-password-email.html"
    subject_template_name = "emails/reset-password-subject.txt"
    form_class = forms.CustomPasswordResetForm


class ResetPasswordDone(PasswordResetDoneView):
    template_name = "users/reset-password-done.html"


# 폐기된 인증메일 다시 누르면 너무 못생김.
class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = "users/reset-password-confirm.html"
    success_url = reverse_lazy("users:reset-password-success")
    prefix = {"uidb64", "token"}


class ResetPasswordSuccess(PasswordResetCompleteView):
    template_name = "users/reset-password-success.html"


@login_required(login_url="/users/login/")
def delete_account(request):

    if request.method == "POST":
        form = forms.DeleteAccountForm(
            request.user, request.POST
        )  # !) request.POST 넣어줘야하는 이유..?

        if form.is_valid():
            request.user.delete()
            logout(request)
            return redirect(reverse("core:home"))
    else:
        form = forms.DeleteAccountForm(request.user)

    return render(request, "users/delete-account.html", {"form": form})


# Login with the Google account

"""
class GoogleException(Exception):
    pass


def google_login(request):
    client_id = os.environ.get("GOOGLE_OAUTH_ID")
    redirect_uri = os.environ.get("GOOGLE_OAUTH_REDIR_URI")
    scope = os.environ.get("GOOGLE_OAUTH_SCOPE")
    response_type = "code"
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}&scope={scope}"
    )


def google_callback(request):
    try:
        data = {
            "code": request.GET.get("code"),
            "client_id": os.environ.get("GOOGLE_OAUTH_ID"),
            "client_secret": os.environ.get("GOOGLE_OAUTH_PW"),
            "redirect_uri": os.environ.get("GOOGLE_OAUTH_REDIR_URI"),
            "grant_type": "authorization_code",
        }
        request_token = requests.post("https://oauth2.googleapis.com/token", data=data)
        token_json = request_token.json()
        print(token_json)
        error = token_json.get("error", None)
        if error is not None:
            raise GoogleException()
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://www.googleapis.com/auth/userinfo.profile",
            headers={"Authorization": f"Bearer {access_token}"},
        ).json()
        print(json.loads(profile_request))
    except GoogleException:
        redirect(reverse("users:login"))
"""
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, View, FormView
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from . import models
from . import forms

# Create your views here.


class StudentProfile(DetailView):

    """UserProfile Definition"""

    model = models.User
    template_name = "users/student_profile.html"

    def get_queryset(self):
        return (
            super().get_queryset().filter(account_type="student")
        )  # get_quryset 메소드를 orverride 하여 계정타입이 stdunet 인 user들만 가져옴.


class StudentList(ListView):

    """UserList Definition"""

    model = models.User
    paginate_by = 20
    ordering = None
    context_object_name = "users"
    template_name = "users/student_list.html"

    def get_queryset(self):
        return (
            super().get_queryset().filter(account_type="student")
        )  # get_quryset 메소드를 orverride 하여 계정타입이 stdunet 인 user들만 가져옴.

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
        context["start_index"] = start_index
        context["next_index"] = end_index + 1
        context["max_index"] = max_index
        # context["object_number_range"] = object_number_range

        return context


class SearchView(View):

    """SearchView Definition"""

    def get(self, request):

        keyword = self.request.GET.get("keyword")  # url에서 keyword 파라미터 값 들고오기.

        if keyword:  # keyword 값이 비어있지 않다면

            result_qs = models.User.objects.filter(
                Q(first_name__contains=keyword) | Q(last_name__contains=keyword)
            ).order_by(
                "-date_joined"
            )  # keyword와 일치하는 오브젝트들의 쿼리셋 만들기.

            # paginator 생성
            page_numbers_range = 10
            paginator = Paginator(result_qs, page_numbers_range)
            page = self.request.GET.get("page", 1)
            max_index = paginator.num_pages
            users = paginator.get_page(page)

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
                "users/user_search.html",
                {
                    "users": users,
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
                "users/user_search.html",
                {"keyword": keyword, "start_index": 0},
            )


class LoginView(FormView):

    """LoginView Definition"""

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")  # !)reverse_lazy 와 reverse 의 차이?

    def form_valid(self, form):
        email = form.cleaned_data.get("email")  # form으로부터 clean된 email data를 받아옴.
        password = form.cleaned_data.get(
            "password"
        )  # form으로부터 clean된 password data를 받아옴.
        user = authenticate(
            self.request, username=email, password=password
        )  # login 인증 부분
        if user is not None:
            login(self.request, user)  # login 시키기
        return super().form_valid(form)  # 최종적으로 form_valid 가 유효하다면 succes_url로 넘겨주기

    pass


def log_out(request):  # logout은 fbv로만 가능.
    logout(request)
    return redirect(reverse("core:home"))


def sign_up(request):
    return render(request, "users/signup.html")


class StudentSignupView(FormView):

    """StudentSignupView Definition"""

    template_name = "users/student_signup.html"
    form_class = forms.StudentSignUpForm
    success_url = reverse_lazy("core:home")

    def form_vaild(self, form):
        form.save()  # !) form.save 는 왜 하는거야?
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

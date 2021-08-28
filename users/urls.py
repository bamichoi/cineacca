from django.urls import path
from users import views as user_views

app_name = "users"
urlpatterns = [
    path("students/", user_views.StudentListView.as_view(), name="list"),
    path(
        "users/profile/<int:pk>",
        user_views.UserProfileView.as_view(),
        name="user_profile",
    ),
    path(
        "students/<int:pk>",
        user_views.StudentProfileView.as_view(),
        name="student_profile",
    ),
    path("students/search/", user_views.SearchView.as_view(), name="search"),
    path("users/login/", user_views.LoginView.as_view(), name="login"),
    path("users/logout/", user_views.log_out, name="logout"),
    path("users/signup/", user_views.sign_up, name="signup"),
    path(
        "users/signup/student",
        user_views.StudentSignupView.as_view(),
        name="student_signup",
    ),
]

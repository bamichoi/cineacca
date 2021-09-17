from django.urls import path
from users import views as user_views

app_name = "users"
urlpatterns = [
    path("students/", user_views.StudentListView.as_view(), name="list"),
    path(
        "users/profile/<int:pk>/",
        user_views.UserProfileView.as_view(),
        name="user_profile",
    ),
    path(
        "users/profile/update/",
        user_views.UpdateProfileView.as_view(),
        name="update_profile",
    ),
    path(
        "users/profile/change-password/",
        user_views.ChangePasswordView.as_view(),
        name="change_password",
    ),
    path(
        "students/<int:pk>/",
        user_views.StudentProfileView.as_view(),
        name="student_profile",
    ),
    path("students/search/", user_views.SearchView.as_view(), name="search"),
    path("users/login/", user_views.LoginView.as_view(), name="login"),
    path("users/logout/", user_views.log_out, name="logout"),
    path("users/signup/", user_views.sign_up, name="signup"),
    path(
        "users/signup/student/",
        user_views.StudentSignupView.as_view(),
        name="student_signup",
    ),
    path(
        "users/signup/public/",
        user_views.PublicSignupView.as_view(),
        name="public_signup",
    ),
    path("users/signup/success/", user_views.signup_success, name="signup_success"),
    path("users/verify/<str:key>", user_views.user_verified, name="verficated"),
    path(
        "users/profile/<int:pk>/send_verify_email/",
        user_views.send_verify_email,
        name="send_verify_email",
    ),
]

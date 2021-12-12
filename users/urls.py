from django.urls import path
from users import views as user_views

app_name = "users"
urlpatterns = [
    path("students/", user_views.StudentListView.as_view(), name="list"),
    path(
        "profile/<int:pk>/",
        user_views.UserProfileView.as_view(),
        name="user_profile",
    ),
    path(
        "profile/<int:pk>/dashboard/",
        user_views.UserDashBoardView.as_view(),
        name="dashboard",
    ),
    path(
        "profile/<int:pk>/dashboard/<str:list_by>/",
        user_views.UserDashBoardList.as_view(),
        name="dashboard_list",
    ),
    path(
        "profile/update/",
        user_views.UpdateProfileView.as_view(),
        name="update_profile",
    ),
    path(
        "profile/change-password/",
        user_views.ChangePasswordView.as_view(),
        name="change_password",
    ),
    path("students/search/", user_views.SearchView.as_view(), name="search"),
    path("login/", user_views.LoginView.as_view(), name="login"),
    path("logout/", user_views.log_out, name="logout"),
    path("signup/", user_views.sign_up, name="signup"),
    path(
        "signup/student/",
        user_views.StudentSignupView.as_view(),
        name="student_signup",
    ),
    path(
        "signup/public/",
        user_views.PublicSignupView.as_view(),
        name="public_signup",
    ),
    path("signup/success/", user_views.signup_success, name="signup_success"),
    path("verify/<str:key>", user_views.user_verified, name="verficated"),
    path(
        "profile/<int:pk>/send_verify_email/",
        user_views.send_verify_email,
        name="send_verify_email",
    ),
    path(
        "reset-password",
        user_views.ResetPasswordView.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password/done",
        user_views.ResetPasswordDone.as_view(),
        name="reset-password-done",
    ),
    path(
        "reset-password/confirm/<uidb64>/<token>/",
        user_views.ResetPasswordConfirm.as_view(),
        name="reset-password-confirm",
    ),
    path(
        "reset-password/success",
        user_views.ResetPasswordSuccess.as_view(),
        name="reset-password-success",
    ),
    path(
        "profile/update/delete",
        user_views.delete_account,
        name="delete-account",
    ),
    
]

"""
    path("login/google", user_views.google_login, name="google-login"),
    path(
        "login/google/callback",
        user_views.google_callback,
        name="google-callback",
    ),"""
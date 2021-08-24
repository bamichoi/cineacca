from django.urls import path
from users import views as user_views

app_name = "users"
urlpatterns = [
    path("students/", user_views.StudentList.as_view(), name="list"),
    path(
        "students/<int:pk>", user_views.StudentProfile.as_view(), name="student_profile"
    ),
    path("students/search/", user_views.SearchView.as_view(), name="search"),
    path("users/login/", user_views.LoginView.as_view(), name="login"),
    path("users/logout/", user_views.log_out, name="logout"),
]

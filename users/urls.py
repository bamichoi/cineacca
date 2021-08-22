from django.urls import path
from users import views as user_views

app_name = "users"
urlpatterns = [
    path("students/", user_views.StudentList.as_view(), name="list"),
    path(
        "students/<int:pk>", user_views.StudentProfile.as_view(), name="student_profile"
    ),
]

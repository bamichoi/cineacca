from django.urls import path
from users import views as user_views

app_name = "users"
urlpatterns = [
    path("people/", user_views.UserList.as_view(), name="list"),
]

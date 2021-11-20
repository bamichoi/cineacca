from django.urls import path
from movies import views as movie_views
from . import views as core_views

app_name = "core"
urlpatterns = [
    path("", movie_views.HomeView.as_view(), name="home"),
    path("upload/", core_views.upload_select_view, name="upload"),
]

from django.urls import path, re_path
from . import views as movie_views

app_name = "movies"
urlpatterns = [
    path("", movie_views.MovieList.as_view(), name="list"),
    path("<int:pk>/", movie_views.MovieDetail.as_view(), name="detail"),
    path(
        "search/",
        movie_views.SearchView.as_view(),
        name="search",
    ),
    path("upload/", movie_views.MovieUpload.as_view(), name="upload"),
    path(
        "<int:pk>/update/",
        movie_views.UpdateMovie.as_view(),
        name="update",
    ),
    path("<int:pk>/delete/", movie_views.delete_movie, name="delete"),
    path("api/movies/<int:pk>/view/", movie_views.count_view, name="count_view"),
    path("api/movies/<int:pk>/fav/", movie_views.switch_fav_view, name="fav"),
]

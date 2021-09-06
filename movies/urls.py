from django.urls import path
from . import views as movie_views

app_name = "movies"
urlpatterns = [
    path("movies/", movie_views.MovieList.as_view(), name="list"),
    path("movies/<int:pk>/", movie_views.MovieDetail.as_view(), name="detail"),
    path("movies/search/", movie_views.SearchView.as_view(), name="search"),
    path("movies/upload/", movie_views.MovieUpload.as_view(), name="upload"),
    path("movies/<int:pk>/update", movie_views.UpdateMovie.as_view(), name="update"),
    path("movies/<int:pk>/delete", movie_views.DeleteMovie.as_view(), name="delete"),
]

from django.urls import path
from movies import views as movie_views

app_name = "movies"
urlpatterns = [
    path("movies/", movie_views.MovieList.as_view(), name="list"),
    path("movies/<int:pk>/", movie_views.MovieDetail.as_view(), name="detail"),
    path("movies/search/", movie_views.SearchView.as_view(), name="search"),
]

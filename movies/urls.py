from django.urls import path
from movies import views as movie_views

app_name = "movies"
urlpatterns = [path("<int:pk>/", movie_views.MovieDetail.as_view(), name="detail")]

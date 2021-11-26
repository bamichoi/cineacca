from django.urls import path, re_path
from . import views as videoart_views

app_name = "videoarts"

urlpatterns = [
    path("", videoart_views.VideoArtList.as_view(), name="list"),
    path("<int:pk>/", videoart_views.VideoArtDetail.as_view(), name="detail"),
    path(
        "search/",
        videoart_views.SearchView.as_view(),
        name="search",
    ),
    path("upload/", videoart_views.VideoArtUpload.as_view(), name="upload"),
    path(
        "<int:pk>/update/",
        videoart_views.UpdateVideoArt.as_view(),
        name="update",
    ),
    path("<int:pk>/delete/", videoart_views.delete_videoart, name="delete"),
    path("api/videoarts/<int:pk>/view/", videoart_views.count_view, name="count_view"),
    path("api/videoarts/<int:pk>/fav/", videoart_views.switch_fav_view, name="fav"),
]

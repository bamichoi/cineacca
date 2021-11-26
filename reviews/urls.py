from django.urls import path
from . import views as review_views

app_name = "reviews"
urlpatterns = [
    path(
        "",
        review_views.ReviewList.as_view(),
        name="list",
    ),
    path(
        "movie/",
        review_views.MovieReviewList.as_view(),
        name="list-movie",
    ),
    path(
        "videoart/",
        review_views.VideoArtReviewList.as_view(),
        name="list-videoart",
    ),
    path(
        "movie/<int:pk>/",
        review_views.MovieReviewDetail.as_view(),
        name="detail-movie",
    ),
    path(
        "videoart/<int:pk>/",
        review_views.VideoArtReviewDetail.as_view(),
        name="detail-videoart",
    ),
    path(
        "api/<int:pk>/review/create/",
        review_views.create_review,
        name="create",
    ),
    path(
        "api/review/delete/",
        review_views.delete_review,
        name="delete",
    ),
    path(
        "api/review/update/",
        review_views.update_review,
        name="update",
    ),
    path("api/reviews/<int:pk>/fav/", review_views.switch_fav_view, name="fav"),
]

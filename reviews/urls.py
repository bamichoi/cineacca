from django.urls import path
from . import views as review_views

app_name = "reviews"
urlpatterns = [
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

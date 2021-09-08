from django.urls import path
from . import views as review_views

app_name = "reviews"
urlpatterns = [
    path(
        "movies/<int:pk>/review/write/",
        review_views.create_review,
        name="create",
    ),
    path(
        "movies/<int:pk>/review/delete/<int:review_pk>",
        review_views.delete_review,
        name="delete",
    ),
    path(
        "api/review/update/",
        review_views.update_review,
        name="update",
    ),
]

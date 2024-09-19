from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post_list/", views.PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("like/<slug:slug>/", views.like_post, name="like_post"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
]

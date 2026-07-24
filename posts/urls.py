from django.urls import path
from .views import CreatePostView, FeedView, RetrievePostView, UpdatePostView, DeletePostView,LikePostView,UnlikePostView


urlpatterns = [
    path("create/", CreatePostView.as_view(), name="create-post"),
    path("feed/",FeedView.as_view(), name = "feed"),
    path("<int:pk>/",RetrievePostView.as_view(), name="retrieve-post"),
    path("<int:pk>/update/",UpdatePostView.as_view(), name="update-post"),
    path("<int:pk>/delete/",DeletePostView.as_view(), name="delete-post"),
    path("<int:pk>/like/",LikePostView.as_view(),name="like-post"),
    path("<int:pk>/unlike/",UnlikePostView.as_view(),name="unlike-post"),
]
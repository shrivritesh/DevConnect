from django.urls import path
from .views import CreatePostView , FeedView , RetrievePostView


urlpatterns = [
    path("", CreatePostView.as_view(), name="create-post"),
    path("feed/",FeedView.as_view(), name = "feed"),
    path("<int:pk>/",RetrievePostView.as_view(), name="retrieve-Post"),
]
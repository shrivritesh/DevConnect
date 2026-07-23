from django.urls import path
from .views import CreatePostView , FeedView , RetrievePostView ,UpdatePostView , DeletePostView


urlpatterns = [
    path("create/", CreatePostView.as_view(), name="create-post"),
    path("feed/",FeedView.as_view(), name = "feed"),
    path("<int:pk>/",RetrievePostView.as_view(), name="retrieve-post"),
    path("<int:pk>/update/",UpdatePostView.as_view(), name="update-post"),
    path("<int:pk>/delete/",DeletePostView.as_view(), name="delete-post"),

]
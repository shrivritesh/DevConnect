from rest_framework.generics import CreateAPIView , ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer


class CreatePostView(CreateAPIView):
    """API view for creating a new post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class FeedView(ListAPIView):
    """API view for listing all posts."""

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return (
            Post.objects.select_related("user").order_by("-created_at")
        )
    # queryset = Post.objects.all()

    # def get_queryset(self):
    #     return Post.objects.all().order_by("-created_at")
    
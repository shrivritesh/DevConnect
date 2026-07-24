from rest_framework.generics import CreateAPIView , ListAPIView , RetrieveAPIView ,UpdateAPIView , DestroyAPIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post , Like
from .serializers import PostSerializer
from .permission import IsOwner


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
    
class RetrievePostView(RetrieveAPIView):
    """
    API view for retrieving a single post.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Post.objects.select_related("user")
        )
    

class UpdatePostView(UpdateAPIView):
    """
    API view for updating post
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return (Post.objects.select_related("user"))
    

class DeletePostView(DestroyAPIView):
    """
    API for deleting Post
    """
    permission_classes = [IsAuthenticated,IsOwner]

    def get_queryset(self):
        return (Post.objects.select_related("user"))


class LikePostView(APIView):
    """
    API view for liking Post
    """
    permission_classes = [IsAuthenticated]

    def post(self,request,pk):
        post = Post.objects.get(pk=pk)

        _, created = Like.objects.get_or_create(user=request.user,post=post,)

        if created:
            return Response(
                {"message": "Post liked successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "You have already liked this post."},
            status=status.HTTP_200_OK,
        )
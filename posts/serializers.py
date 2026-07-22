from rest_framework import serializers
from .models import Post
from accounts.serializers import UserMiniSerializer

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for creating, retrieving,
    updating, and validating posts.
    """

    user=UserMiniSerializer(read_only = True)
    class Meta:
        """
        Configuration options for the Post serializer.
        """
        model = Post
        fields = (
            "id",
            "user",
            "caption",
            "image",
            "file",
            "created_at",
            "updated_at",
        )

        """
        Read-only fields are included in the API output, but should not be included in the input during create or update operations.
        Any 'read_only' fields that are incorrectly included in the serializer input will be ignored.
        """
        read_only_fields = (
            "id",
            "user",
            "created_at",
            "updated_at",
        )

    def validate(self, attrs):
        """
        Ensure that a post contains at least one of:
        caption, image, or file.
        """
        caption = attrs.get("caption")
        image = attrs.get("image")
        file = attrs.get("file")

        if not caption and not image and not file:
            raise serializers.ValidationError("A post must contain at least one of: caption, image, or file. ")
        return attrs
    
        # if (
        #     not attrs.get("caption")
        #     and not attrs.get("image")
        #     and not attrs.get("file")
        # ):
        #     


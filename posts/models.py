from django.conf import settings
from django.db import models


class Post(models.Model):

    """
    Represents a post created by a user.

    A post can contain a caption, an image, a file attachment,
    or any combination of them.
    
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    caption = models.TextField(
        max_length=1000,
        blank=True,
    )

    image = models.ImageField(
        upload_to="posts/images/",
        blank=True,
        null=True,
    )

    file = models.FileField(
        upload_to="posts/files/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        """
        Return a human-readable representation of the post.
        """
        if self.caption:
            return f"{self.user.email} - {self.caption[:30]}"
        return f"{self.user.email} - Post #{self.id}"
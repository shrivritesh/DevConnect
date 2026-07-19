from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):

    """
    Admin configuration for the Post model.
    """

    list_display=(
        "id",
        "user",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "caption",
    )

    list_filter =(
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
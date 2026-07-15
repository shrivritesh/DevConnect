from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.
    Email is used as the unique identifier for authentication instead of username.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        create and save regular user with the given email and password

        """
        if not email:
            raise ValueError("Users must have an email address.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save superuser with the given fields

        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(
            email=email,
            password=password,
            **extra_fields
        )

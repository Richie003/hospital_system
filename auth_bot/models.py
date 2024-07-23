from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create_user method creates and saves new user objects."""
        if not email:
            raise ValueError("User must have valid email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)  # Save the user object after setting the fields

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class UserBio(models.Model):
    for_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="userbio", on_delete=models.CASCADE
    )
    address = models.CharField(default="No.2 Ally lane...", max_length=255, blank=True)
    address2 = models.CharField(
        default="No.2 JohnDoe Close...", max_length=255, blank=True
    )
    tel = models.CharField(default="", max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.for_user)

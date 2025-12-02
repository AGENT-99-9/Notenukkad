from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, phone, email, full_name, password=None, **extra_fields):
        if not phone:
            raise ValueError("Phone number is required")
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(phone, email, full_name, password, **extra_fields)

class User(AbstractUser):
    username = None  # remove username
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)

    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "full_name"]
    favorites = models.ManyToManyField(
        'listings.Listing',
        related_name='liked_by',
        blank=True
    )

    objects = UserManager()

    def __str__(self):
        return f"{self.full_name} ({self.phone})"


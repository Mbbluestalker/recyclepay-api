from db.models.user_manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=255, null=True)
    otp = models.CharField(null=True, max_length=6)
    profile_image = models.URLField(null=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    is_individual = models.BooleanField(default=False)
    is_collector = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    points_earned = models.FloatField(default=0.0)

    def user_type(self):
        group = (
            "individual"
            if self.is_individual
            else "collector"
            if self.is_collector
            else "partner"
            if self.is_partner
            else "admin"
            if self.is_admin
            else ""
        )

        return group

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ["-created_at"]

        

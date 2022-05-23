from db.models.categories_model import Category
from db.models.user_model import User
from django.db import models

STATUS_CHOICES = [
    ("pending", "Pending"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
    ("cancelled", "Cancelled"),
    ("completed", "Completed"),
]


class Order(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    weight_in_kg = models.FloatField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="pending")
    requested_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"is_partner": True, "is_individual": True},
        related_name="requested_by",
    )
    picked_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        limit_choices_to={"is_collector": True},
        related_name="picked_by",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

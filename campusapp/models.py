from django.db import models
from django.contrib.auth.models import User


class LostFoundItem(models.Model):

    ITEM_TYPES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Claimed', 'Claimed'),
        ('Returned', 'Returned'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)

    item_type = models.CharField(
        max_length=10,
        choices=ITEM_TYPES
    )

    how_lost = models.TextField(
        blank=True
    )

    description = models.TextField()

    location = models.CharField(
        max_length=200
    )

    current_location = models.CharField(
        max_length=200,
        blank=True
    )

    latitude = models.FloatField(
        blank=True,
        null=True
    )

    longitude = models.FloatField(
        blank=True,
        null=True
    )

    date = models.DateField()

    contact = models.CharField(
        max_length=20
    )

    image = models.ImageField(
        upload_to='items/',
        blank=True,
        null=True
    )

    estimated_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
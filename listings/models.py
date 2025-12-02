from django.db import models
from django.conf import settings

class Listing(models.Model):
    CATEGORY_CHOICES = (
        ('BOOK', 'Book'),
        ('NOTE', 'Notes'),
        ('OTHER', 'Other'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # denormalized location (copied from seller at creation time)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='listings'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.category} - {self.pincode}"

    class Meta:
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['pincode']),
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']  # newest first

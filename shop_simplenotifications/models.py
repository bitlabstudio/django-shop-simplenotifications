"""Models for shop_simplenotifications application."""

from django.db import models


class Example(models.Model):
    """Example model class."""
    text = models.TextField(blank=True, null=True)


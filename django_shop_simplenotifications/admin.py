"""Admin classes for django_shop_simplenotifications application."""

from django.contrib import admin

from django_shop_simplenotifications.models import Example


class ExampleAdmin(admin.ModelAdmin):
    """Admin class for Example model class."""
    pass


admin.site.register(Example, ExampleAdmin)

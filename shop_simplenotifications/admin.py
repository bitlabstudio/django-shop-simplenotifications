"""Admin classes for shop_simplenotifications application."""

from django.contrib import admin

from .models import Example


class ExampleAdmin(admin.ModelAdmin):
    """Admin class for Example model class."""
    pass


admin.site.register(Example, ExampleAdmin)


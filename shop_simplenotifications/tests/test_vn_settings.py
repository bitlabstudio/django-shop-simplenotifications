from settings import *

ADMINS = (('John', 'john@example.com'),)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

SOUTH_TESTS_MIGRATE = False


#!/usr/bin/env python
import os, sys
from django.conf import settings


DIRNAME = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    DATABASES={
       "default": {
           "ENGINE": "django.db.backends.sqlite3",
           "NAME": ":memory:",
       }
    },
    ADMINS=(('John', 'john@example.com'),),
    SOUTH_TESTS_MIGRATE=False,
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'shop',
        'shop_simplenotifications',)
)


from django.test.simple import run_tests

failures = run_tests(['shop_simplenotifications',], verbosity=1)
if failures:
    sys.exit(failures)


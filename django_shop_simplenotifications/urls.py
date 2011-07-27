"""URLs for django_shop_simplenotifications application."""

from django.conf.urls.defaults import *


urlpatterns = patterns('django_shop_simplenotifications.views',
    url(r'^$', view='index', name='django_shop_simplenotifications_index'),
)

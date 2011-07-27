"""URLs for shop_simplenotifications application."""

from django.conf.urls.defaults import *


urlpatterns = patterns('shop_simplenotifications.views',
    url(r'^$', view='index', name='shop_simplenotifications_index'),
)


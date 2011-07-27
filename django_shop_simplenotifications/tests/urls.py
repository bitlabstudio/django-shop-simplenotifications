from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^example/', include('django_shop_simplenotifications.urls')),
)

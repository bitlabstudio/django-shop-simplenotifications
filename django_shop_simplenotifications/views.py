"""Views for django_shop_simplenotifications application."""

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list


from django_shop_simplenotifications.models import Example


def index(request, template_name='django_shop_simplenotifications/example_list.html'):
    """Index view."""
    qs = Example.objects.all()

    try:
        page = int(request.GET.get('page', 0))
    except ValueError:
        raise Http404

    return object_list(
        request,
        queryset=qs,
        template_object_name='example',
	paginate_by=10,
 	page=page,        
    )

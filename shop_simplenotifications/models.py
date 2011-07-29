#-*- coding: utf-8 -*-
"""Signal handlers for shop_simplenotifications."""
from django.conf import settings
from django.core.mail import send_mail

from shop.order_signals import confirmed


def confirmed_email_notification(sender, **kwargs):
    """
    Sends an email notification to the shop owner when a new order is
    completed.
    """
    from_email = getattr(settings, 'SN_FROM_EMAIL',
                         settings.DEFAULT_FROM_EMAIL)
    owners = getattr(settings, 'SN_OWNERS', settings.ADMINS)
    send_mail('Subject here', 'Here is the message.', from_email,
            [owner[1] for owner in owners], fail_silently=False)

confirmed.connect(confirmed_email_notification)


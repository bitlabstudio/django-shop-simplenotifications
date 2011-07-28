#-*- coding: utf-8 -*-
"""Signal handlers for shop_simplenotifications."""
from django.core.mail import send_mail

from shop.order_signals import confirmed


def confirmed_email_notification(sender, **kwargs):
    """
    Sends an email notification to the shop owner when a new order is
    completed.
    """
    send_mail('Subject here', 'Here is the message.', 'from@example.com',
            ['to@example.com'], fail_silently=False)

confirmed.connect(confirmed_email_notification)


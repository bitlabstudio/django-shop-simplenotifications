#-*- coding: utf-8 -*-
"""Test cases for the signal handlers."""
import decimal
from unittest import TestCase

from django.contrib.auth.models import User
from django.core import mail

from shop.models.ordermodel import Order
from shop.order_signals import confirmed
from shop.tests.util import Mock

class ConfirmedTestCase(TestCase):
    """
    Test case for the signal handler that sends a notification to the shop
    owner when a order has been placed.
    """
    def setUp(self):
        self.user = User.objects.create(
                username="test", 
                email="test@example.com")
        self.request = Mock()
        setattr(self.request, 'user', None)
        self.order = Order()
        self.order.order_subtotal = decimal.Decimal('10')
        self.order.order_total = decimal.Decimal('10')
        self.order.shipping_cost = decimal.Decimal('0')

        self.order.shipping_address_text = 'shipping address example'
        self.order.billing_address_text = 'billing address example'

        self.order.save()

    def test_should_send_email_on_confirmed_signal(self):
        confirmed.send(sender=self, order=self.order)
        self.assertEqual(len(mail.outbox), 1)


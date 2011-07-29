#-*- coding: utf-8 -*-
"""Test cases for the signal handlers."""
import decimal

from django.conf import settings
from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase

from shop.models.ordermodel import Order
from shop.order_signals import confirmed
from shop.tests.util import Mock
from shop.tests.utils.context_managers import SettingsOverride


class SignalHandlerBaseTestCase(object):
    """
    Base test case class for test classes that test signal handlers.
    """
    def setUp(self):
        self.user = User.objects.create(
                username="test",
                email="test@example.com")
        self.request = Mock()
        setattr(self.request, 'user', self.user)
        self.order = Order()
        self.order.user = self.user
        self.order.order_subtotal = decimal.Decimal('10')
        self.order.order_total = decimal.Decimal('10')
        self.order.shipping_cost = decimal.Decimal('0')

        self.order.shipping_address_text = 'shipping address example'
        self.order.billing_address_text = 'billing address example'

        self.order.save()


class PaymentInstructionsTestCase(SignalHandlerBaseTestCase, TestCase):
    """
    Test case for the signal handler that sends payment instructions to the
    customer when an order has been placed.
    """
    def test_should_send_email_confirmed_signal(self):
        confirmed.send(sender=self, order=self.order)
        self.assertEqual(len(mail.outbox), 2)

    def test_should_have_from_address_from_settings(self):
        from_email = 'noreply@myshop.com'
        with SettingsOverride(SN_FROM_EMAIL=from_email):
            confirmed.send(sender=self, order=self.order)
            self.assertEqual(mail.outbox[0].from_email, from_email)

    def test_should_send_email_to_customer(self):
        confirmed.send(sender=self, order=self.order)
        self.assertEqual(mail.outbox[1].to, ['test@example.com',])

    def test_has_subject_from_template(self):
        confirmed.send(sender=self, order=self.order)
        self.assertEqual(mail.outbox[1].subject, 'Your order at MyShop.com')

    def test_has_body_from_template(self):
        confirmed.send(sender=self, order=self.order)
        self.assertTrue('Dear Customer' in mail.outbox[1].body)


class ConfirmedTestCase(SignalHandlerBaseTestCase, TestCase):
    """
    Test case for the signal handler that sends a notification to the shop
    owner when an order has been placed.
    """
    def test_should_send_email_on_confirmed_signal(self):
        confirmed.send(sender=self, order=self.order)
        self.assertEqual(len(mail.outbox), 2)

    def test_should_have_from_address_from_settings(self):
        from_email = 'noreply@myshop.com'
        with SettingsOverride(SN_FROM_EMAIL=from_email):
            confirmed.send(sender=self, order=self.order)
            self.assertEqual(mail.outbox[0].from_email, from_email)

    def test_should_send_email_to_owners(self):
        owners = (('John', 'john@example.com'), ('Mary', 'mary@example.com'))
        with SettingsOverride(SN_OWNERS=owners):
            confirmed.send(sender=self, order=self.order)
            self.assertEqual(len(mail.outbox[0].to), 2)

    def test_has_subject_from_template(self):
        confirmed.send(sender=self, order=self.order)
        self.assertEqual(mail.outbox[0].subject, 'New order has been placed')

    def test_has_body_from_template(self):
        confirmed.send(sender=self, order=self.order)
        self.assertTrue('Dear Shop-Owner' in mail.outbox[0].body)


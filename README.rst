django-shop-simplenotifications
================================

Do not use this, yet!

This is a dead simple approach on email notifications for django-shop. The
goal of this app is to hook into django-shop's various signals in order to 
send emails to the shop owner and to the buyer on certain events.

Installation
=============

Install this package into your virtualenv::

  pip install -e git+git://github.com/mbrochh/django-shop-simplenotifications.git#egg=shop_simplenotifications

Add the app to your INSTALLED_APPS setting::

  INSTALLED_APPS = (
      ...
      'shop_simplenotifications',
  )

Configuration
==============

SN_FROM_EMAIL
++++++++++++++

Default: DEFAULT_FROM_EMAIL

The from address for your automated emails. Example::

  SN_EMAIL_FROM = 'noreply@myshop.com'

SN_OWNERS
++++++++++

Default: ADMINS

A tuple that lists people who get notifications about new incoming orders and
payments. Each member of the tuple should be a tuple of
(Full name, email address). Example::

  (('John', 'john@example.com'), ('Mary', 'mary@example.com'))

Features
=========

  * When a buyer completes his order, the shop owner gets a notification mail

Testing
========

Currently this app does not ship with a test-project. If you want to test this
app, please add it to the ``INSTALLED_APPS`` of your Django project, copy the
file ``test_sn_settings`` into your apps root folder  and run
``./manage.py test --settings=test_sn_settings shop_simplenotifications``. 
Sorry for that. Will fix it soon.

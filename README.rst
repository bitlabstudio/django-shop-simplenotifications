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

Templates
==========

In order to easily provide notifications with the wording and formatting of
your choice, there are templates for all email subjects and bodies. In order
to override the defaults, add the folowing templates to your
``templates/shop_simplenotifications/`` folder:

  * confirmed_subject.html
  * confirmed_body.html

Features
=========

  * When a buyer completes his order, the shop owners get a notification mail
  * All notification emails can be easily templated.

Testing
========

Currently I don't provide any bootstrapping script, so you will need to setup
a virtual environment that has at least django and django-shop installed.

Once that is setup just run ``/runtests.sh``

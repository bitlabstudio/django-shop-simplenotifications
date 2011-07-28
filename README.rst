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

Features
=========

  * When a buyer completes his order, the shop owner gets a notification mail


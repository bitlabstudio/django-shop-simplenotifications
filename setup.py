import os
from setuptools import setup, find_packages
import shop_simplenotifications


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="shop_simplenotifications",
    version=shop_simplenotifications.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='django,django-shop,email,notifications',
    packages=find_packages(),
    author='Martin Brochhaus',
    author_email='martin.brochhaus@gmail.com',
    url="https://github.com/mbrochh/django-shop-simplenotifications",
    include_package_data=True,
)

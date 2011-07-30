import os
from setuptools import setup, find_packages
import shop_simplenotifications


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

# List of classifiers: http://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications :: Email',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

# Detailed instructions: http://docs.python.org/distutils/setupscript.html
setup(
    name="shop_simplenotifications",
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    version=shop_simplenotifications.__version__,
    install_requires=[
        'django-cms==2.1.3',
        #TODO martin: comment in this line as soon as 0.0.10 is on PyPi
        #'django-shop',
    ],

    author='Martin Brochhaus',
    author_email='martin.brochhaus@gmail.com',
    url="https://github.com/mbrochh/django-shop-simplenotifications",

    license='BSD License',
    platforms=['OS Independent'],
    keywords='django,django-shop,email,notifications',
    classifiers=CLASSIFIERS,

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

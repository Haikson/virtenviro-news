from distutils.core import setup
from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = []


setup(
    name='virtenviro-news',
    version="0.1.0"
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    url='http://www.virtenviro.org/',
    license='GPL3',
    author='Kamo Petrosyan',
    author_email='kamo@haikson.com',
    description='A Django News application. Created for Virtenviro.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'django>=1.9',
        'django-mptt',
        'django-filebrowser-no-grappelli',
        'lxml',
        'Pillow',
        'pytils',
        'django-datetime-widget',
    ]
)

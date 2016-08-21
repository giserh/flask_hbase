#! /user/bin/env python
#encoding=utf8

from setuptools import setup

setup(
    name='Flask-Hbase',
    version='0.1.0',
    url='https://github.com/howardyan93/flask-hbase',
    author='Howard Yan',
    author_email='porcp93@outlook.com',
    maintainer='Howard Yan',
    maintainer_email='porcp93@outlook.com',
    download_url='https://github.com/howardyan93/flask-hbase/releases',
    description='Hbase Extension for Flask Applications by using happybase',
    packages=['flask_hbase'],
    package_data={'': ['LICENSE']},
    zip_safe=False,
    install_requires=[
        'Flask>=0.1.0',
        'redis>=2.7.6',
    ],
    classifiers=[
        'Development Status :: 1 - Init',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

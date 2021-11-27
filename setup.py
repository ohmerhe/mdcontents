#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='mdcontents',
    version='0.0.1',
    author='ohmer',
    author_email='ohmerhe@google.com',
    url='https://ohmerhe.com',
    description=u'markdown to structured contents',
    packages=['mdcontents'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mdcontents=mdcontents:json',
        ]
    }
)
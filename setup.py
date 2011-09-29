#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad

import setuptools

setuptools.setup(
    name='debt',
    version=__import__('debt').__version__,
    license='GNU Lesser General Public License (LGPL), Version 3',

    install_requires=['SQLAlchemy>=0.6.6','pysqlite'],
    provides=['debt'],

    description='Debt Management G.U.I',
    long_description=open('README.rst').read(),

    url='http://github.com/fadiga/debt',

    packages=['debt'],

    classifiers=[
        'License :: OSI Approved :: GNU Library or '
        'Lesser General Public License (LGPL)',
        'Programming Language :: Python',
    ],
)

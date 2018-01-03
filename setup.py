#!/usr/bin/env python2
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

setup(
    name='admin_couchdb',
    version='0.0.1',
    description='Short description',
    long_description=''.join(open('README.rst').readlines()),
    keywords='couchdb, replication',
    author='Oleh Horbachov',
    author_email='gorbyo@gmail.com',
    license='GPLv3',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ],
    requires=['couchdb', 'couchquery', 'requests']
)

#!/bin/python2.7
# -*- coding: utf-8 -*-
"""
EIOP 2022 -- 
"""

import sys
import os
import codecs


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


packages = [
    'news_parser',
]

with open('requirements.txt') as f:
    required = []
    for line in f:
        line = line.strip()
        # let's also ignore empty lines and comments
        if not line or line.startswith('#'):
            continue
        if 'https://' in line:
            tail = line.rsplit('/', 1)[1]
            tail = tail.split('#')[0]
            line = tail.replace('@', '==').replace('.git', '')
        required.append(line)


with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()


setup(
    name='news_parser',
    version='0.5.4',
    description='Extracts data from an article file',
    long_description=readme,
    author='Ivan Sedelkin, Mohammed Shakir, Suad Huseynli',
    author_email='ivan.sedelkin9@gmail.com, mohammedshakir010528@gmail.com, suadreal@gmail.com',
    url='https://github.com/RyuTribal/news_scraper',
    packages=packages,
    include_package_data=True,
    install_requires=required,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: Swedish',
        'Intended Audience :: Developers',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)

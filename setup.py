#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Whitev2
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2023 Whitev2
"""

version = '1.0.0'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='async-openai',
    version=version,

    author='Whitev2',
    author_email='maksfundd@gmail.com',

    description=(
        u'Python module for asynchronous interaction with OpenAI '
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Whitev2/async-openai',
    download_url='https://github.com/Whitev2/async-openai/archive/v{}/main.zip'.format(version),

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['async-openai'],
    install_requires=['aiohttp'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
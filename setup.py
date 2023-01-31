#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Whitev2
:MIT License, see LICENSE file
:copyright: (c) 2023 Whitev2
"""

version = '1.1.8'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ai_openchat',
    version=version,

    author='Whitev2',
    author_email='maksfundd@gmail.com',

    description=(
        u'Python module for asynchronous interaction with OpenAI '
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Whitev2/async-openai',
    download_url='https://github.com/Whitev2/async-openai/archive/refs/tags/v.{}.zip'.format(version),

    license='MIT License, see LICENSE file',

    packages=['ai_openchat'],
    install_requires=['aiohttp>=3.8.3'],

    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
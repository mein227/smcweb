#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-smcweb',
    version='0.1.0',
    author='Mein hsu',
    author_email='mein227@gmail.com',
    maintainer='Mein hsu',
    maintainer_email='mein227@gmail.com',
    license='BSD-3',
    url='https://github.com/mein227/pytest-smcweb',
    description='SMC WEB plugin with Pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_smcweb'],
    install_requires=['pytest>=2.9.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'pytest11': [
            'smcweb = pytest_smcweb',
        ],
    },
)

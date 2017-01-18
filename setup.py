#!/usr/bin/env python
from setuptools import setup
import sys
from os import path

if sys.version_info < (3, 5):
    raise RuntimeError("Python < 3.5 is not supported!")

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst')) as file:
    long_description = file.read()

setup(
    name='deasync',
    version='1.0.1',
    description="deasync decorator to make async functions/methods synchronous.",
    long_description=long_description,
    url='https://github.com/prokopst/deasync',
    py_modules=['deasync'],
    author="Stanislav Prokop",
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="async await deasync desynchronize",
    test_suite='tests',
    setup_requires=['nose']
)

#!/usr/bin/env python
from setuptools import setup
import sys

if sys.version_info < (3, 5):
    raise RuntimeError("Python < 3.5 is not supported!")


setup(
    name='deasync',
    version='0.1.0',
    description="deasync decorator to make async functions/methods synchronous.",
    url='https://github.com/prokopst/deasync',
    py_modules=['deasync'],
    author='Stanislav Prokop',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="async await deasync desynchronize",
    test_suite="tests",
)

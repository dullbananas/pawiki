#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pawiki',
    version='1.0',
    packages=find_packages(),

    install_requires = [
        'wiki',
    ]
)

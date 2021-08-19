# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:29:31 2021

@author: user24
"""

from setuptools import setup

setup(
    name='toshokan',
    author='Cube Team',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'myscript=myscript:run'
        ]
    }
)



#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "tornadoredischat",
    version = "0.0.1-SNAPSHOT",
    packages = find_packages('src'),
    package_dir = { '': 'src'},
    install_requires = ['setuptools', 
        'django == 1.5',
        'tornado-redis == 2.4.5',
        'tornado == 3.1',
        'redis == 2.7.6',
    ],
    entry_points = {
        'console_scripts': (
            'runserver = tornadoredischat.tornadoapp:main',
        )
    },
)

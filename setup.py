# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'gereedschapcentrum',
    version      = '1.0',
    packages     = find_packages(),
    package_data={
        'gereedschapcentrum' : ['resources/*.csv']
    },
    entry_points = {
        'scrapy': ['settings = gereedschapcentrum.settings']
    },
    zip_safe=False,
)


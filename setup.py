# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'Gereedschapcentrum',
    version      = '1.0',
    packages     = find_packages(),
    package_data={
        'Gereedschapcentrum' : ['resources/*.csv']
    },
    entry_points = {
        'scrapy': ['settings = Gereedschapcentrum.settings']
    },
    zip_safe=False,
)


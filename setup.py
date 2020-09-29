# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "db_micro"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="SHI Backend Server",
    author_email="sam@shi.health.com",
    url="",
    keywords=["Swagger", "SHI Backend Server"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['db_micro=db_micro.__main__:main']},
    long_description="""\
    SHI backend server description.
    """
)


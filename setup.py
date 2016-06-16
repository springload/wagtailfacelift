import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtailfacelift',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Facelift for Wagtail streamfields.',
    long_description=README,
    url='https://github.com/springload/wagtailfacelift',
    author='Josh Barr',
    author_email='josh@springload.co.nz',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)

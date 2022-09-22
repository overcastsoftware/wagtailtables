import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Package dependencies
install_requires = [
    'wagtail>=1.8',
]

# Testing dependencies
testing_extras = [
]

# Documentation dependencies
documentation_extras = [
]

setup(
    name='wagtailtables',
    version='0.2.1',
    packages=['wagtailtables'],
    include_package_data=True,
    license='MIT',
    description='jSpreadsheet table blocks for Wagtail',
    long_description=README,
    url='https://github.com/overcast/wagtailtables/',
    author='Overcast',
    author_email='hallo@overcast.is',
    long_description_content_type="text/markdown",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Framework :: Wagtail :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras
    },
)

# python3-library-starter
[![Build Status](https://travis-ci.org/org_CHANGEME/repo_CHANGEME.svg?branch=master)](https://travis-ci.org/org_CHANGEME/repo_CHANGEME)
[![PyPI version](https://badge.fury.io/py/pypi_name_CHANGEME.svg)](https://badge.fury.io/py/pypi_name_CHANGEME)

Simple Python 3 library starter

## Prerequisites
* `Python 3.7`
* [`virtualenv`](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

## Usage
```bash
git clone git@github.com:k-t-corp/python3-library-starter.git
cd python3-library-starter
rm -rf .git
nano setup.py  # pay close attention to the CHANGEME's
mv python3_library_starter pypi_name  # rename the library package name, of course.
nano README.md  # change readme, of course. pay close attention to CHANGEME's in urls of the badges.
git init
python3 -m virtualenv venv
source venv/bin/activate
python setup.py develop
```

## Setup publishing library to PyPI via Travis CI
1. Make sure the library name doesn't clash
2. Create a new token on PyPI
3. Enable the project on Travis CI
4. Run `travis encrypt <token> --add deploy.password`
5. Commit and push the change

## Publish the library to PyPI via Travis CI
Just create a new GitHub release

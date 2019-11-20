from setuptools import setup, find_packages

install_requires = [
    'Random-Word==1.0.4',
]

setup(
    name='pypi-name-CHANGEME',
    version='1.0',
    url='http://github.com/org_CHANGEME/repo_CHANGEME',
    author='CHANGEME',
    author_email='CHANGEME',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires
)

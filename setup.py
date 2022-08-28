from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='SE HW 1',
    version='1.0',
    description='SE HW 1',
    long_description=readme,
    author='SE Group 10',
    url='https://github.com/boscosylvester-john/se_hw1',
    packages=find_packages(exclude=('tests', 'docs'))
)
from setuptools import setup

setup(
    name='pyactions',
    version='1.0.0',
    description='Declarative builder for Github Action Scripts',
    author='Julien Bongars',
    packages=['pyactions'],
    install_requires=[
        "dataclasses==0.6"
    ],
)

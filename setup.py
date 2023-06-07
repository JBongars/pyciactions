from setuptools import setup

setup(
    name='pyciactions',
    version='1.0.0',
    description='Declarative builder for Github Action Scripts',
    author='Julien Bongars',
    packages=['pyactions'],
    install_requires=[
        "dataclasses==0.6",
        "PyYAML==6.0"
    ],
)

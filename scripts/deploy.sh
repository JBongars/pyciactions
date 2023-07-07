#!/bin/bash

# script to deploy pacakge to pip

script_dir=$(dirname "$0")
username=$2
password=$3

if [ -z "$username" ]; then
    read -p "Username: " username
fi

if [ -z "$password" ]; then
    read -s -p "Password: " password
fi

(
    cd "$script_dir/.."

    python setup.py sdist bdist_wheel
    pip install twine

    twine upload -u $username -p $password --skip-existing --verbose dist/*

    rm -rf dist build *.egg-info
)
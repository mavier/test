#!/bin/bash
set -e
set -x

if [[ "${TOX_ENV}" == "pypy"* ]]; then
    sudo add-apt-repository -y ppa:pypy/ppa
    sudo apt-get -y update
    sudo apt-get install -y pypy pypy-dev

    sudo rm -rf /usr/local/pypy/bin
fi

pip install tox

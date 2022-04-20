#!/bin/bash

export PYTHONPATH=/app/

flake8 --ignore E24,W504,E501 --exclude=tests .
flakeExit=$?

if [ $flakeExit -ne 0 ]; then
    echo "flake error"
    exit $flakeExit
fi

# coverage run -m pytest
# coverage report -m
# coverage --rcfile=/app/tests/.coveragerc report
# coverage --cov-config=/app/tests/.coveragerc
pytest --cov-report term-missing --cov=app --cov-config=/app/tests/.coveragerc tests/

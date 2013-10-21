#!/bin/sh
echo """
\tThis seeks to be a master script for running the development site locally.
Please pay attention to the appropriate variables and email me if necessary.
Be careful not to commit and external libraries to version control.
Our VC should exclusively be focused on our custom codebase.
"""
echo "Setting up virtual environment & external packages"
set -x
virtualenv --no-site-packages --python=python3.3 dev_env
. dev_env/bin/activate
pip install -r requirements/local.txt

echo "Creating the database"
sudo -u postgres dropdb gameguides
sudo -u postgres createdb gameguides -T template0 -E UTF8

echo "Use these:
echo "./game_guides/manage.py syncdb"
echo "./game_guides/manage.py migrate"
echo "and ./game_guides/manage.py runserver --settings=game_guides.settings.local"
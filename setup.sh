#!/bin/zsh
echo """
\tThis seeks to be a master script for running the development site locally.
Please pay attention to the appropriate variables and email me if necessary.
Be careful not to commit any external libraries to version control.
Our VC should exclusively be focused on our custom codebase.
"""
echo "Setting up virtual environment & external packages"
echo "Make sure you are in the proper virtualenv"
pip install -r requirements/local.txt

echo "Creating the database"
brew install postgres
pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
dropdb gameguides
createdb gameguides -T template0 -E UTF8

echo "./game_guides/manage.py syncdb 
./game_guides/manage.py migrate" # Need to fix some import issue so that these can be run inline
echo "Use ./game_guides/manage.py runserver --settings=game_guides.settings.local"
echo "./manage.py graph_models -a -g -o netcode_visual.png will make a pretty picture of the schema"


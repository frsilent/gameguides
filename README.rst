========================
Netcode Illuminati Rewrite
========================

A project for the serving of premium video content for the purposed of improving player skills in a variety of online video games.

To use this project follow these steps:

#. Create your working environment
#. git clone the project
#. Install Django
#. Install additional dependencies
#. Run with ./manage.py runserver --settings test

Working Environment
===================

You have several options in setting up your working environment.  It is recommended to
use virtualenv to separate the dependencies of the project from that of the system's
python environment.  If on Linux or Mac OS X, you can also use virtualenvwrapper to help manage multiple virtualenvs across different projects.

Virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv --distribute game_guides

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.

Virtualenv with virtualenvwrapper
--------------------------

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
which will take care of managing your virtual environments and adding the
project path to the `site-directory` for you::

    $ mkdir nci
    $ mkvirtualenv -a nci nci-dev
    $ cd nci && add2virtualenv `pwd`

Windows
----------

In Windows, or if you're not comfortable using the command line, you will need
to add a `.pth` file to the `site-packages` of your virtualenv. Your
virtualenv folder will be something like::

`~/.virtualenvs/nci/lib/python3.3/site-directory/`

In the pathfile, you will want to include the following code (from
virtualenvwrapper):

    import sys; sys.__plen = len(sys.path)
    /home/<youruser>/game_guides/nci/
    import sys; new=sys.path[sys.__plen:]; del sys.path[sys.__plen:]; p=getattr(sys,'__egginsert',0); sys.path[p:p]=new; sys.__egginsert = p+len(new)

git clone
=================

To download the site in its present form use the command:

    $ git clone https://github.com/frsilent/game_guides.git
    At any time to update:
    $ git pull

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Acknowledgements
================
-Casey Foster for his work on the site layout
-Aaron Schank and Roland Heintze for the code base
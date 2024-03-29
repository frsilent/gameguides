import os, sys

sys.path.append('/var/www/gameguides')
sys.path.append('/var/www/gameguides/game_guides')

os.environ['DJANGO_SETTINGS_MODULE'] = 'game_guides.settings.demo'
os.environ['PYTHON_EGG_CACHE'] = '/var/www/gameguides/cache'
os.environ['DEFAULT_CACHE_ALIAS'] = '/var/www/gameguides/cache'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

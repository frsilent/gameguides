import os, sys

sys.path.append('/var/www/gameguides')
sys.path.append('/var/www/gameguides/game_guides')

os.environ['DJANGO_SETTINGS_MODULE'] = 'game_guides.settings.production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
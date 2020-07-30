#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/twitter-monitor-app')

from flaskapp import app as application
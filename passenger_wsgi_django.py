import sys, os

DOMAIN_ROOT = os.environ.get('DOMAIN_ROOT')
PROJECTNAME = 'myproject'  # fill with your project name
SRCDIR = os.path.join(DOMAIN_ROOT, PROJECTNAME)
VENV = os.path.join(DOMAIN_ROOT, '.virtualenv')
INTERP = os.path.join(VENV, 'bin', 'python3')

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.join(VENV, 'lib', 'python3.6', 'site-packages'))
sys.path.insert(0, SRCDIR)

# Launch the django project
os.environ['DJANGO_SETTINGS_MODULE'] = PROJECTNAME + '.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

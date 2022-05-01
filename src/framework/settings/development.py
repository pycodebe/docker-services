from .common import *

DEBUG=True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'django',]

INSTALLED_APPS += ['debug_toolbar',]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
INTERNAL_IPS = ['127.0.0.1', 'localhost', ]

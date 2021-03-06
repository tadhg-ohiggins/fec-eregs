from .base import *

DEBUG = True
INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)

# Analytics settings

CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'
CACHES['eregs_longterm_cache']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'
CACHES['api_cache']['TIMEOUT'] = 5  # roughly per request

try:
    from local_settings import *
except ImportError:
    pass

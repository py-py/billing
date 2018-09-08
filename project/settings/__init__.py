from .base import *

ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')

if ENVIRONMENT == 'production':
    from .production import *
if ENVIRONMENT == 'dev':
    from .dev import *

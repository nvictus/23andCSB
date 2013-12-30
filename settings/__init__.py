import os
env = os.environ.get('ENVIRONMENT', 'DEVELOPMENT')

if env == 'PRODUCTION':
    from .prod import *
else:
    from .dev import *


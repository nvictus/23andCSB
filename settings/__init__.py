import os
env = os.environ.get('ENVIRONMENT', 'development')

if env == 'production':
    from .prod import *
else:
    from .dev import *


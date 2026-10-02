from .base import *

# Production settings

DEBUG = True

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

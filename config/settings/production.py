from .base import *

# Production settings

DEBUG = False

# Hosts and CSRF
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

CSRF_TRUSTED_ORIGINS = env.list(
    'CSRF_TRUSTED_ORIGINS', 
    default=[],
)

# Secure cookie
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HTTPS
SECURE_SSL_REDIRECT = env.bool(
    "SECURE_SSL_REDIRECT",
    default=False,
)

# SECURE_HSTS_SECONDS = True
from .base import *

# Development settings

DEBUG = True

ALLOWED_HOSTS = env.list(
    'ALLOWED_HOSTS',
    default=[
        "localhost",
        "127.0.0.1",
        "0.0.0.0",
    ],
)


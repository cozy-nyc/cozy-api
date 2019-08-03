import socket

from .base import *


# Webpack Loader by Owais Lane
# ------------------------------------------------------------------------------
# https://github.com/owais/django-webpack-loader

WEBPACK_LOADER = {
            'DEFAULT': {
                        'BUNDLE_DIR_NAME': 'builds-dev/',
                                'STATS_FILE': os.path.join(BASE_DIR, 'webpack', 'webpack-stats.dev.json')
                                    }
            }



INTERNAL_IPS = ['127.0.0.1', '10.0.2.2',]



ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')

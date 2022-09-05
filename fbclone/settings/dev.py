from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'fbclone',
        'USER':'postgres',
        'PASSWORD':'psql',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

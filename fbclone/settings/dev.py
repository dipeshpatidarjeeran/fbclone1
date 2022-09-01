from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'postgres',
        'USER':'fbclone',
        'PASSWORD':'fbclone',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

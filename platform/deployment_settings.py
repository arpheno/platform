SECRET_KEY = '@9n+09e2kdo*3l2fhhbg68i^+b95su%8($te#q6339&amp;7i+3-z4'
from shared_settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'data',
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'admin',                  # Not used with sqlite3.
        'HOST': '',
        'PORT': '',
    }
}


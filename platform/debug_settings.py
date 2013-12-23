SECRET_KEY = '@9n+09e2kdo*3l2fhhbg68i^+b95su%8($te#q6339&amp;7i+3-z4'
from shared_settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


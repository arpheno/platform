import os
SECRET_KEY = '@9n+09e2kdo*3l2fhhbg68i^+b95su%8($te#q6339&amp;7i+3-z4'
from elfinder.utils.accesscontrol import fs_standard_access
from elfinder.volumes.filesystem import ElfinderVolumeLocalFileSystem
DEBUG = True
TEMPLATE_DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_URLCONF = 'trt.urls'
WSGI_APPLICATION = 'trt.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'materials',
    'training',
    'account',
    'elfinder',
    'gunicorn',
    'sorl.thumbnail'
)
AUTH_USER_MODEL = 'account.TrtUser'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'trtplatform@gmail.com'
EMAIL_HOST_PASSWORD = 'trainersrule'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_ROOT = os.path.join(BASE_DIR, 'serve', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
CONTEXT_PROCESSORS = ('django.core.context_processors.csrf')
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s: %(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'trt': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

TIME_ZONE = 'CET'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True

ELFINDER_CONNECTOR_OPTION_SETS = {
    'admin': {
        'debug': False,
        'roots': [
            {
                'alias': 'Trainings',
                'id': 'lft',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'trainings'),
                'URL': '%strainings/' % MEDIA_URL,
                'uploadMaxSize': '128m',
            },
            {
                'alias': 'Resources',
                'id': 'lfr',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'resources'),
                'URL': '%sresources/' % MEDIA_URL,
            },
            {
                'alias': 'New Files',
                'id': 'lfs',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'staging'),
                'URL': '%sstaging/' % MEDIA_URL,
            },
            {
                'alias': 'Internal',
                'id': 'lfi',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'internal'),
                'URL': '%sinternal/' % MEDIA_URL,
            },
            {
                'alias': 'Public',
                'id': 'lfp',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'public'),
                'URL': '%spublic/' % MEDIA_URL,
            },
        ]
    },
    'staff': {
        'debug': False,
        'roots': [
            {
                'alias': 'Trainings',
                'id': 'lft',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'trainings'),
                'URL': '%strainings/' % MEDIA_URL,
            },
            {
                'alias': 'Resources',
                'id': 'lfr',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'resources'),
                'URL': '%sresources/' % MEDIA_URL,
            },
            {
                'alias': 'New Files',
                'id': 'lfs',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'staging'),
                'URL': '%sstaging/' % MEDIA_URL,
            },
            {
                'alias': 'Internal',
                'id': 'lfi',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'internal'),
                'URL': '%sinternal/' % MEDIA_URL,
            },
            {
                'alias': 'Public',
                'attributes': [{
                    'pattern': r'\.*',
                    'read': True,
                    'write': True,
                }],
                'id': 'lfp',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'public'),
                'URL': '%spublic/' % MEDIA_URL,
            },
        ]
    },
    'trainer': {
        # optionally set debug to True for additional debug messages
        'debug': False,
        'roots': [
            {
                'alias': 'Trainings',
                'attributes': [{
                    'pattern': r'.*',
                    'read': True,
                    'write': False,
                    'locked': True
                    }],
                'id': 'lft',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'trainings'),
                'URL': '%strainings/' % MEDIA_URL,
                },
            {
                'alias': 'Resources',
                'attributes': [{
                    'pattern': r',*',
                    'read': True,
                    'write': False,
                    'locked': True
                    }],
                'id': 'lfr',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'resources'),
                'URL': '%sresources/' % MEDIA_URL,
                },
            {
                'alias': 'New Files',
                'id': 'lfs',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'staging'),
                'URL': '%sstaging/' % MEDIA_URL,
                },
            {
                'alias': 'Internal',
                'attributes': [{
                    'pattern': r'\.*',
                    'read': True,
                    'write': True,
                    }],
                'id': 'lfi',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'internal'),
                'URL': '%sinternal/' % MEDIA_URL,
                },
            {
                'alias': 'Public',
                'attributes': [{
                    'pattern': r'\.*',
                    'read': True,
                    'write': False,
                    'locked': True
                    }],
                'id': 'lfp',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'public'),
                'URL': '%spublic/' % MEDIA_URL,
                },
        ]
        },
    'eestecer': {
        # optionally set debug to True for additional debug messages
        'debug': False,
        'roots': [
            {
                'alias': 'Internal',
                'attributes': [{
                    'pattern': r'\.*',
                    'read': True,
                    'write': False,
                    'locked': True
                    }],
                'id': 'lfi',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'internal'),
                'URL': '%sinternal/' % MEDIA_URL,
                },
            {
                'alias': 'Public',
                'attributes': [{
                    'pattern': r'\.*',
                    'read': True,
                    'write': False,
                    'locked': True
                    }],
                'id': 'lfp',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'public'),
                'URL': '%spublic/' % MEDIA_URL,
                },
            ]
        },
    'anon': {
        # optionally set debug to True for additional debug messages
        'debug': False,
        'roots': [
            {
                'alias': 'Public',
                'attributes': [{
                    'pattern': r'\.*',
                    'read': True,
                    'write': False,
                    'locked': True
                    }],
                'id': 'lfp',
                'driver': ElfinderVolumeLocalFileSystem,
                'path': os.path.join(MEDIA_ROOT, u'public'),
                'URL': '%spublic/' % MEDIA_URL,
                },
            ]  # end roots
        },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

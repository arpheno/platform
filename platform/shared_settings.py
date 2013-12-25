import os
from elfinder.utils.accesscontrol import fs_standard_access
from elfinder.volumes.filesystem import ElfinderVolumeLocalFileSystem

DEBUG = True
TEMPLATE_DEBUG = DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_URLCONF = 'platform.urls'
WSGI_APPLICATION = 'platform.wsgi.application'

INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'news',
        'materials',
        'history',
        'account',
        'elfinder'
        )
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(BASE_DIR, 'serve','static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',)
TEMPLATE_DIRS = ( os.path.join(BASE_DIR, 'templates'),)
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
                'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt' : "%d/%b/%Y %H:%M:%S"
                },
            },
        'handlers': {
            'null': {
                'level':'DEBUG',
                'class':'django.utils.log.NullHandler',
                },
            'logfile': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': BASE_DIR + "/logfile",
                'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
                },
            'console':{
                'level':'INFO',
                'class':'logging.StreamHandler',
                'formatter': 'standard'
                },
            },
        'loggers': {
            'django': {
                'handlers':['console'],
                'propagate': True,
                'level':'WARN',
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
        'admin' : {
            'debug' : False, #optionally set debug to True for additional debug messages
            'roots' : [
                {
                    'alias' : 'Trainings',
                    'id' : 'lft',
                    'driver' : ElfinderVolumeLocalFileSystem,
                    'path' : os.path.join(MEDIA_ROOT, u'trainings'),
                    'URL' : '%strainings/' % MEDIA_URL,
                    'uploadMaxSize' : '128m',
                    'accessControl' : fs_standard_access,
                    'archivers' : {},
                    },
                {
                    'alias' : 'Resources',
                    'id' : 'lfr',
                    'driver' : ElfinderVolumeLocalFileSystem,
                    'path' : os.path.join(MEDIA_ROOT, u'resources'),
                    'URL' : '%sresources/' % MEDIA_URL,
                    'uploadAllow' : ['all',],
                    'uploadDeny' : ['all',],
                    'uploadOrder' : ['deny', 'allow'],
                    'uploadMaxSize' : '128m',
                    'accessControl' : fs_standard_access,
                    'archivers' : {},
                    },
                {
                    'alias' : 'New Files',
                    'id' : 'lfs',
                    'driver' : ElfinderVolumeLocalFileSystem,
                    'path' : os.path.join(MEDIA_ROOT, u'staging'),
                    'URL' : '%sstaging/' % MEDIA_URL,
                    'uploadAllow' : ['all',],
                    'uploadDeny' : ['all',],
                    'uploadOrder' : ['deny', 'allow'],
                    'uploadMaxSize' : '128m',
                    'accessControl' : fs_standard_access,
                    'archivers' : {},
                    },
                {
                    'alias' : 'Internal',
                    'id' : 'lfi',
                    'driver' : ElfinderVolumeLocalFileSystem,
                    'path' : os.path.join(MEDIA_ROOT, u'internal'),
                    'URL' : '%sinternal/' % MEDIA_URL,
                    'uploadAllow' : ['all',],
                    'uploadDeny' : ['all',],
                    'uploadOrder' : ['deny', 'allow'],
                    'uploadMaxSize' : '128m',
                    'accessControl' : fs_standard_access,
                    'archivers' : {},
                    },
                {
                        'alias' : 'Public',
                        'attributes' : [{
                            'pattern' : r'\.*',
                            'read' : True,
                            'write': True,
                            }],
                        'id' : 'lfp',
                        'id' : 'lfp',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'public'),
                        'URL' : '%spublic/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                ]#end roots
    },
        'staff' : {
                'debug' : False, #optionally set debug to True for additional debug messages
                'roots' : [
                    {
                        'alias' : 'Trainings',
                        'id' : 'lft',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'trainings'),
                        'URL' : '%strainings/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    {
                        'alias' : 'Resources',
                        'id' : 'lfr',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'resources'),
                        'URL' : '%sresources/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    {
                        'alias' : 'New Files',
                        'id' : 'lfs',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'staging'),
                        'URL' : '%sstaging/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    {
                        'alias' : 'Internal',
                        'id' : 'lfi',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'internal'),
                        'URL' : '%sinternal/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    {
                            'alias' : 'Public',
                            'attributes' : [{
                                'pattern' : r'\.*',
                                'read' : True,
                                'write': True,
                                }],
                            'id' : 'lfp',
                            'driver' : ElfinderVolumeLocalFileSystem,
                            'path' : os.path.join(MEDIA_ROOT, u'public'),
                            'URL' : '%spublic/' % MEDIA_URL,
                            'uploadAllow' : ['all',],
                            'uploadDeny' : ['all',],
                            'uploadOrder' : ['deny', 'allow'],
                            'uploadMaxSize' : '128m',
                            'accessControl' : fs_standard_access,
                            'archivers' : {},
                            },
                    ]#end roots
    },
        'trainer' : {
                'debug' : False, #optionally set debug to True for additional debug messages
                'roots' : [
                    {
                        'alias' : 'Trainings',
                        'attributes' : [{
                            'pattern' : r'.*',
                            'read' : True,
                            'write': False,
                            'locked' : True
                            }],
                        'id' : 'lft',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'trainings'),
                        'URL' : '%strainings/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    {
                        'alias' : 'Resources',
                        'attributes' : [{
                            'pattern' : r',*',
                            'read' : True,
                            'write': False,
                            'locked' : True
                            }],
                        'id' : 'lfr',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'resources'),
                        'URL' : '%sresources/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    {
                        'alias' : 'New Files',
                        'id' : 'lfs',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'staging'),
                        'URL' : '%sstaging/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    {
                            'alias' : 'Internal',
                            'attributes' : [{
                                'pattern' : r'\.*',
                                'read' : True,
                                'write': True,
                                }],
                            'id' : 'lfi',
                            'driver' : ElfinderVolumeLocalFileSystem,
                            'path' : os.path.join(MEDIA_ROOT, u'internal'),
                            'URL' : '%sinternal/' % MEDIA_URL,
                            'uploadAllow' : ['all',],
                            'uploadDeny' : ['all',],
                            'uploadOrder' : ['deny', 'allow'],
                            'uploadMaxSize' : '128m',
                            'accessControl' : fs_standard_access,
                            'archivers' : {},
                            },
                    {
                            'alias' : 'Public',
                            'attributes' : [{
                                'pattern' : r'\.*',
                                'read' : True,
                                'write': False,
                                'locked' : True
                                }],
                            'id' : 'lfp',
                            'driver' : ElfinderVolumeLocalFileSystem,
                            'path' : os.path.join(MEDIA_ROOT, u'public'),
                            'URL' : '%spublic/' % MEDIA_URL,
                            'uploadAllow' : ['all',],
                            'uploadDeny' : ['all',],
                            'uploadOrder' : ['deny', 'allow'],
                            'uploadMaxSize' : '128m',
                            'accessControl' : fs_standard_access,
                            'archivers' : {},
                            },
                    ]#end roots
    },
        'eestecer' : {
                'debug' : False, #optionally set debug to True for additional debug messages
                'roots' : [
                    {
                        'alias' : 'Internal',
                        'attributes' : [{
                            'pattern' : r'\.*',
                            'read' : True,
                            'write': False,
                            'locked' : True
                            }],
                        'id' : 'lfi',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'internal'),
                        'URL' : '%sinternal/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    {
                        'alias' : 'Public',
                        'attributes' : [{
                            'pattern' : r'\.*',
                            'read' : True,
                            'write': False,
                            'locked' : True
                            }],
                        'id' : 'lfp',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'public'),
                        'URL' : '%spublic/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    ]#end roots
                },
        'anon' : {
                'debug' : False, #optionally set debug to True for additional debug messages
                'roots' : [
                    {
                        'alias' : 'Public',
                        'attributes' : [{
                            'pattern' : r'\.*',
                            'read' : True,
                            'write': False,
                            'locked' : True
                            }],
                        'id' : 'lfp',
                        'driver' : ElfinderVolumeLocalFileSystem,
                        'path' : os.path.join(MEDIA_ROOT, u'public'),
                        'URL' : '%spublic/' % MEDIA_URL,
                        'uploadAllow' : ['all',],
                        'uploadDeny' : ['all',],
                        'uploadOrder' : ['deny', 'allow'],
                        'uploadMaxSize' : '128m',
                        'accessControl' : fs_standard_access,
                        'archivers' : {},
                        },
                    ]#end roots
                },
        }#end optionsets
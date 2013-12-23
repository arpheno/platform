# Django settings for example_project project.
import os
from os.path import join
from django.conf import settings
from elfinder.utils.accesscontrol import fs_standard_access
from elfinder.volumes.filesystem import ElfinderVolumeLocalFileSystem

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DIRNAME = os.path.dirname(__file__)
PROJECT_ROOT = os.path.normpath(os.path.join(DIRNAME,'..'))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join('data'),                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'admin',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@9n+09e2kdo*3l2fhhbg68i^+b95su%8($te#q6339&amp;7i+3-z4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'platform.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'platform.wsgi.application'

TEMPLATE_DIRS = (
        PROJECT_ROOT + '/templates/',
        )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'materials',
    'news',
    'history',
    'elfinder'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
            'filename': PROJECT_ROOT + "/logfile",
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


#ELFINDER STUFF

#OPTIONAL - An example of a custom option set that allows only pdf files
#and stores them in a special 'pdf' folder
from elfinder.utils.accesscontrol import fs_standard_access
ELFINDER_CONNECTOR_OPTION_SETS = {
        'admin' : {
            'debug' : False, #optionally set debug to True for additional debug messages
            'roots' : [
                {
                    'alias' : 'Trainings',
                    'id' : 'lft',
                    'driver' : ElfinderVolumeLocalFileSystem,
                    'path' : join(MEDIA_ROOT, u'trainings'),
                    'URL' : '%strainings/' % MEDIA_ROOT,
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
                    'path' : join(MEDIA_ROOT, u'resources'),
                    'URL' : '%sresources/' % settings.MEDIA_URL,
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
                    'path' : join(MEDIA_ROOT, u'staging'),
                    'URL' : '%sstaging/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'internal'),
                        'URL' : '%sinternal/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'public'),
                        'URL' : '%spublic/' % settings.MEDIA_URL,
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
                    'path' : join(MEDIA_ROOT, u'trainings'),
                    'URL' : '%strainings/' % settings.MEDIA_URL,
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
                    'path' : join(MEDIA_ROOT, u'resources'),
                    'URL' : '%sresources/' % settings.MEDIA_URL,
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
                    'path' : join(MEDIA_ROOT, u'staging'),
                    'URL' : '%sstaging/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'internal'),
                        'URL' : '%sinternal/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'public'),
                        'URL' : '%spublic/' % settings.MEDIA_URL,
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
                    'path' : join(MEDIA_ROOT, u'trainings'),
                    'URL' : '%strainings/' % settings.MEDIA_URL,
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
                    'path' : join(MEDIA_ROOT, u'resources'),
                    'URL' : '%sresources/' % settings.MEDIA_URL,
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
                    'path' : join(MEDIA_ROOT, u'staging'),
                    'URL' : '%sstaging/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'internal'),
                        'URL' : '%sinternal/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'public'),
                        'URL' : '%spublic/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'internal'),
                        'URL' : '%sinternal/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'public'),
                        'URL' : '%spublic/' % settings.MEDIA_URL,
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
                        'path' : join(MEDIA_ROOT, u'public'),
                        'URL' : '%spublic/' % settings.MEDIA_URL,
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

import os
from os.path import dirname, join, abspath

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_DIR = dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'projectdb',
    }
}

TIME_ZONE = 'America/Chicago'
STATIC_URL = '/static/'
TEMPLATE_DIRS = (join(PROJECT_DIR, 'templates'), )
STATIC_DIR = (join(PROJECT_DIR, 'static'), )
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = '-2cmgs7l$5grqwd!cyat6&6241^ah&rwn#ef5s_lm(1@0a4w&v'

MIDDLEWARE= (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [abspath(join(PROJECT_DIR, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'multiselect',
    'django_nose',
    'example.sample',
)

SOUTH_TESTS_MIGRATE = False

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

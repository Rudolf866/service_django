# *************************************** #
#      DJANGO 3.2     Python 3.10         #
# *************************************** #


# *************************************** #
#           ADMINISTRATOR                 #
# --------------------------------------- #
#          USERNAME:  admin_django        #
#          PASSWORD:  admin_django        #
# *************************************** #


# *************************************** #
#    Инициализация переменные среды       #
# *************************************** #

import os
from pathlib import Path
from dotenv import load_dotenv
from corsheaders.defaults import default_headers

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.abspath(BASE_DIR / '.env'))

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

# *************************************** #
#       Application definition            #
# *************************************** #

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'corsheaders',
    'rest_framework',
    'app',
]

# *************************************** #
#          MIDDLEWARE SETTINGS            #
# *************************************** #

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# *************************************** #
#           DATABASE SETTINGS             #
# *************************************** #

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME_POSTGRES'),
        'USER': os.getenv('DATABASE_USER_POSTGRES'),
        'PASSWORD': os.getenv('DATABASE_PASS_POSTGRES'),
        'HOST': os.getenv('DATABASE_POSTGRES_HOST'),
        'PORT': os.getenv('DB_PORT_POSTGRES'),
    }
}

# *************************************** #
#         VALIDATION SETTINGS             #
# *************************************** #

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# *************************************** #
#     Internationalization settings       #
# *************************************** #

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# *************************************** #
#       Static files settings             #
# *************************************** #

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# *************************************** #
#           REDIS SETTINGS                #
# *************************************** #
REDIS_HOST_DOCKER = 'redis'
# REDIS_HOST_DOCKER = 'localhost'
REDIS_PORT_DOCKER = '6379'

# *************************************** #
#           CELERY SETTINGS               #
# *************************************** #

CELERY_BROKER_URL = 'redis://' + REDIS_HOST_DOCKER + ':' + REDIS_PORT_DOCKER + '/0'
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST_DOCKER + ':' + REDIS_PORT_DOCKER + '/0'
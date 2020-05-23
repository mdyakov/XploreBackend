import os
import django_heroku
import dj_database_url
import pickle 
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RECOMMENDATIONS_DATA = pd.read_csv("data.csv")

#KNN_MODEL = pickle.load(open(os.path.join(BASE_DIR, 'knn'), 'rb'))

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = (bool)(True if os.environ.get('DEBUG') == 'True' else False)

ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                 'xplore-backend-production.herokuapp.com', 'xplore-backend-staging.herokuapp.com']

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'users_api.apps.UsersApiConfig',
    'games_api.apps.GamesApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST
    'rest_framework.authtoken',  # Required for Token authentication.
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10  # MAX AMMOUNT of objects send with one request.
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'xplore_api.urls'

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

WSGI_APPLICATION = 'xplore_api.wsgi.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LANGUAGE_CODE = 'en-us' 

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

RAPID_API_URL = os.environ.get('RAPID_API_URL')

RAPID_API_HOST = os.environ.get('RAPID_API_HOST')

RAPID_API_KEY = os.environ.get('RAPID_API_KEY')

django_heroku.settings(locals())

if DEBUG:
    del DATABASES['default']['OPTIONS']['sslmode']
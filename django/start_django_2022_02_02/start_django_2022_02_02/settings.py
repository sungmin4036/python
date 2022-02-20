"""
Django settings for start_django_2022_02_02 project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from msilib.schema import Media
from pathlib import Path
from django.urls import reverse_lazy

import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #base 프로젝트 경로

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = "2n6gggvhf@=@tj8l60$lzqf*9*^yi4nwbus+uyb-6s5@-w9cty"

# # Parse database connection url strings
# # like psql://user:pass@127.0.0.1:8458/db
# DATABASES = {
#     # read os.environ['DATABASE_URL'] and raises
#     # ImproperlyConfigured exception if not found
#     #
#     # The db() method is an alias for db_url().
#     'default': env.db(),

#     # read os.environ['SQLITE_URL']
#     'extra': env.db_url(
#         'SQLITE_URL',
#         default='sqlite:////tmp/my-tmp-sqlite.db'
#     )
# }

# CACHES = {
#     # Read os.environ['CACHE_URL'] and raises
#     # ImproperlyConfigured exception if not found.
#     #
#     # The cache() method is an alias for cache_url().
#     'default': env.cache(),

#     # read os.environ['REDIS_URL']
#     'redis': env.cache_url('REDIS_URL')
# }



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# ------------------django-doc 복사 부분



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accountapp',
    'bootstrap4',
    'profileapp',
    'articleapp',
    'commentapp',
    'projectapp',  
    'subscribeapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'start_django_2022_02_02.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'start_django_2022_02_02.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',  // type 에러 떠서 교체
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
# head 연결해줌


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# python manage.py collectstatic 명령어를 사용하면 프로젝트에 있는 모든 static 파일들을 한군대로 모아주는 명령어 인데, 이 명령어를 통해서 이 파일들이 어디로 모이는건지 알려주는것.


# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     '/var/www/static/',
# ]  #기본 django doc 에서 가죠오면 이 형태지만 왜인지 모르지만 /(슬러시)가 나누기로 인식 한다. => ,(콤마)로 변경

STATICFILES_DIRS = [
    BASE_DIR , "static",
    '/var/www/static/',
]

# static files 들을 앱에 종속시키지 않고 static 폴더 따로 관리 하기 위해 설정, django Doc 참조.


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = reverse_lazy('accountapp:hello_world')
LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login')
# 로그인 페이지를 next 인자로 받아서 한게 아닌 url에 직접 입력하여 들어올경우 에러 발생 이것을 방지하기위한 설정
# 직적 /login url로 들어가서도 사용해도, 메인 페이지로 이동해준다. url_redirect 설정.

MEDIA_URL = 'media/' #주소창에 media 이하의 파일에 접속해야지 미디어 파일에 접속 가능하다는것

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # media 파일을 서버에 올렸을때 어느 경로에 저장될것인지에 대한 정보.

# 127.0.01:8000.media/test.jpg
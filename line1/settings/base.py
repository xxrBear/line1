import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(BASE_DIR / '.env')


def required_env(name):
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Environment variable '{name}' is required but not set.")
    return value


SECRET_KEY = "django-insecure-n(sqdhyakh3ph$03a67*cmb0hwd4d)$02$4ulncuhl%-+md76t"

DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "debug_toolbar",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.base',
    'apps.blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "line1.urls"

WSGI_APPLICATION = "line1.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": required_env('POSTGRES_NAME'),
        "HOST": required_env('POSTGRES_HOST'),
        'PORT': required_env('POSTGRES_PORT'),
        'USER': required_env('POSTGRES_USER'),
        'PASSWORD': required_env('POSTGRES_PASSWORD'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://:helloworld@127.0.0.1:6379/0",
    },
    "session_cache": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://:helloworld@127.0.0.1:6379/1",
    },
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SESSION_CACHE_ALIAS = "session_cache"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = False

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------------------------------------------
# 静态文件
# -----------------------------------------------------------------------
STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = BASE_DIR / 'prod_static'

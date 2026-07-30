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
    'apps.users',
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

AUTH_USER_MODEL = 'users.User'

# -----------------------------------------------------------------------
# 静态文件
# -----------------------------------------------------------------------
STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = BASE_DIR / 'prod_static'

# -----------------------------------------------------------------------
# 日志
# -----------------------------------------------------------------------
DJANGO_ENV = 'dev'
LOG_DIR = Path(os.environ.get('DJANGO_LOG_DIR', BASE_DIR / 'logs'))
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_LEVEL = os.environ.get(
    'DJANGO_LOG_LEVEL', 'INFO' if DJANGO_ENV == 'prod' else 'DEBUG'
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '{asctime} [{levelname}] {name} {module}.{funcName}:{lineno} pid={process:d} tid={thread:d} - {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} [{levelname}] {name} - {message}',
            'style': '{',
        },
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)d %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple' if DEBUG else 'json',
        },
        # 日志轮转
        'app_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR / 'app.log',
            'maxBytes': 1024 * 1024 * 20,  # 单文件20MB
            'backupCount': 10,  # 保留10份历史文件
            'formatter': 'json',
            'encoding': 'utf-8',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR / 'error.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 10,
            'formatter': 'json',
            'encoding': 'utf-8',
        },
        # Django请求相关日志(慢查询、500错误等)单独归档
        'django_request_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR / 'django_request.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 10,
            'formatter': 'json',
            'encoding': 'utf-8',
        },
        # SQL查询日志(仅开发环境需要开启)
        'sql_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR / 'sql.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 3,
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
        },
        # 空处理器,可用于临时屏蔽某些库日志
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        # Django核心
        'django': {
            'handlers': ['console', 'app_file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Django请求处理相关(包含500错误、安全警告等)
        'django.request': {
            'handlers': ['console', 'django_request_file'],
            'level': 'WARNING',
            'propagate': False,
        },
        # 安全相关警告(比如CSRF失败、可疑请求等),生产环境必须关注
        'django.security': {
            'handlers': ['console', 'error_file'],
            'level': 'WARNING',
            'propagate': False,
        },
        # SQL查询日志,仅DEBUG模式生效
        'django.db.backends': {
            'handlers': ['sql_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # 服务器相关(runserver的access log),生产环境走Gunicorn access log,这里可关小
        'django.server': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'myapp': {
            'handlers': ['console', 'app_file', 'error_file'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console', 'app_file'],
        'level': LOG_LEVEL,
    },
}

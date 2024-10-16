from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(a05as7xwtkh*%z3jz=fon$5z!3s*g19#p01f$f5b&1sgqe6m0'

MODE = "MIGRATE"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'django_extensions',
    'django_celery_results',
    'corsheaders',
    'rest_framework',
    "drf_spectacular",
    'core.django_populate.infra.populate',
    'core.user',
    'core.posts',
    'core.veterinary',
    'core.uploader',
    'core.supporting_materials',
    'core.quiz',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

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

WSGI_APPLICATION = 'django_project.wsgi.application'



REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("core.user.authentication.TokenAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticatedOrReadOnly",),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "PAGE_SIZE": 10,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Fabrica Histologia",
    "DESCRIPTION": "API para gerenciamento do atlas de Histologia.",
    "VERSION": "1.0.0",
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# App Uploader/Cloudinary settings
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dzdrwmug3',
    'API_KEY': '741644777853926',
    'API_SECRET': 'UvCHKnDuW0NhXZfXgLtOptBmTtc',
    'PREFIX': 'vet',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


if MODE in ["PRODUCTION", "MIGRATE"]:
    CLOUDINARY_URL = "cloudinary://741644777853926:UvCHKnDuW0NhXZfXgLtOptBmTtc@dzdrwmug3"
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    MEDIA_URL = '/images/'
else:
    MY_IP = "127.0.0.1"
    MEDIA_URL = f"http://{MY_IP}:19003/images/"

MEDIA_ENDPOINT = "/images/"
MEDIA_ROOT = os.path.join(BASE_DIR, "images/")
FILE_UPLOAD_PERMISSIONS = 0o640


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
CORS_ALLOW_ALL_ORIGINS = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "user.User"


PASSAGE_APP_ID: str = '2TXjjhFWhntb7WqVkG46xAmb'
PASSAGE_API_KEY: str = 'WG7v8fQtFx.eQpT8x7cBDY3NITVXUGLgEDWSg4eNUGDKzlFIRBfg7P7fUROLPpkgANHLGhCYesq'
PASSAGE_AUTH_STRATEGY: int = 2


EMAIL_BACKEND: str = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST: str = 'smtp.gmail.com'
EMAIL_PORT: int = 587
EMAIL_USE_TLS: bool = True
EMAIL_HOST_USER: str = 'fabricahistologia@gmail.com'
EMAIL_HOST_PASSWORD: str = 'xrnq bkut ihta symq'
EMAIL_RECEIVER_HISTOLOGY_USER: str = "joaovssouza59@gmail.com"
EMAIL_RECEIVER_PATHOLOGY_USER: str = "marcusviniciusgraciano04@gmail.com"

CELERY_TIMEZONE: str = "America/Sao_Paulo"
CELERY_TASK_TRACK_STARTED: bool = True
CELERY_TASK_TIME_LIMIT: int = 30 * 60
CELERY_BROKER_URL: str = 'amqp://jaotarzan:Batata_12@localhost:5672/fabricahistologia'
CELERY_RESULT_BACKEND: str = 'rpc://'

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

MODE = os.getenv("MODE")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["https://fabrica-histologia-backend.fexcompany.me", "http://localhost:8001", "http://127.0.1:8001"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cloudinary_storage",
    "cloudinary",
    "django_extensions",
    "django_celery_results",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "core.django_populate.infra.populate",
    "core.user",
    "core.posts",
    "core.veterinary",
    "core.uploader",
    "core.supporting_materials",
    "core.quiz",
    "django_filters",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("core.user.authentication.TokenAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
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
DATABASE_URL = urlparse(os.getenv("DATABASE_URL"))

if MODE in ["PRODUCTION", "MIGRATE"]:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DATABASE_URL.path.replace("/", ""),
            "USER": DATABASE_URL.username,
            "PASSWORD": DATABASE_URL.password,
            "HOST": DATABASE_URL.hostname,
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = os.getenv("STATIC_URL", "/static/")

# App Uploader/Cloudinary settings
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
    "PREFIX": os.getenv("CLOUDINARY_PREFIX"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


if MODE in ["PRODUCTION", "MIGRATE"]:
    CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")
    DEFAULT_FILE_STORAGE = os.getenv("DEFAULT_FILE_STORAGE")
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_STORAGE = os.getenv("STATICFILES_STORAGE")
    MEDIA_URL = os.getenv("MEDIA_URL", "/images/")
else:
    MY_IP = os.getenv("MY_IP", "127.0.0.1")

    MEDIA_URL = f"http://{MY_IP}:19003/images/"

MEDIA_ENDPOINT = "/images/"
MEDIA_ROOT = os.path.join(BASE_DIR, "images/")
FILE_UPLOAD_PERMISSIONS = 0o640


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
CORS_ALLOW_ALL_ORIGINS = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"

PASSAGE_APP_ID = os.getenv("PASSAGE_APP_ID")
PASSAGE_API_KEY = os.getenv("PASSAGE_API_KEY")
PASSAGE_AUTH_STRATEGY = os.getenv("PASSAGE_AUTH_STRATEGY")


EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_RECEIVER_HISTOLOGY_USER = os.getenv("EMAIL_RECEIVER_HISTOLOGY_USER")
EMAIL_RECEIVER_PATHOLOGY_USER = os.getenv("EMAIL_RECEIVER_PATHOLOGY_USER")


CELERY_TIMEZONE: str = "America/Sao_Paulo"
CELERY_TASK_TRACK_STARTED: bool = True
CELERY_TASK_TIME_LIMIT: int = 30 * 60
# CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

API_URL = os.getenv("API_URL")

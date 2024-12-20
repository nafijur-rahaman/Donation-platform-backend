"""
Django settings for Donation_platform project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()  # Reads the .env file
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["127.0.0.1", 'localhost', '0.0.0.0', ".vercel.app","http://127.0.0.1:5500"]


# Application definition
AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #django apps
    'rest_framework',
    'corsheaders',
    'django_filters',
    'rest_framework.authtoken',
    # cloudinary
    
    'cloudinary_storage',
    'cloudinary',
    
    #custom apps
 
    'campaigns',
    'users',
    'transactions',
    'notification',
    'manager',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # cors middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Donation_platform.urls'

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

WSGI_APPLICATION = 'Donation_platform.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASES = {
#     'default': dj_database_url.config(
#         # Replace this value with your local database's connection string.
#         default='postgresql://donationplatform_user:zWSjqIjUn0G2Fzrl6k9JtNP45nNpHIBg@dpg-cratctdds78s73d9tmjg-a.oregon-postgres.render.com/donationplatform',
#         conn_max_age=600
#     )
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.fhdltlxcfhiakcgopxaz',
        'PASSWORD': 'SKf6Ky7k*Brf8Mh',
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
        'PORT': '6543'
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



# rest framework configurations
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
      'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 20,
  
}



#onrender csrf permission
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5500",
    'http://127.0.0.1:8000',
    'https://donation-platform.netlify.app',
    'https://donation-platform-backend-psi.vercel.app/',
    
]
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'accept',
    'origin',
    'x-csrftoken',
]


CORS_ALLOW_CREDENTIALS = True

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT=BASE_DIR / 'staticfiles'
MEDIA_URL = f'https://res.cloudinary.com/{env("CLOUD_NAME")}/'




DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# sslcomerz setup

# settings.py
SSL_COMMERZ_STORE_ID = 'donat66cde4ca58cbb'
SSL_COMMERZ_STORE_PASSWORD = 'donat66cde4ca58cbb@ssl'
SSL_COMMERZ_SESSION_API = 'https://sandbox.sslcommerz.com/gwprocess/v3/api.php'
SSL_COMMERZ_VALIDATION_API = 'https://sandbox.sslcommerz.com/validator/api/validationserverAPI.php?wsdl'
SSL_COMMERZ_TEST_MODE = True  # Set to False when going live

# email setup

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")

# cloudirnary setup
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': ,  
#     'api_key': 
#     'API_SECRET': ,
# }


import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cloudinary configuration
cloudinary.config(
    cloud_name=env("CLOUD_NAME"),
    api_key=env("API_KEY"),
    api_secret=env("API_SECRET_KEY"),
)

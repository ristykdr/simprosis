"""
Django settings for simprosis project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from distutils.version import StrictVersion
import django

from qr_code.qrcode import constants

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*eqw8)6(qcht6m)zz$)lm_)w9n2plzju9byg)n$atm__2bhfa7'

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
    'rps',
    'biodataDosen',
    'biodataMahasiswa',
    'inputKRS',
    'olahDataDosen',
    'olahDataJurnalKuliah',
    'olahDataMahasiswa',
    'olahDataMatakuliah',
    'olahDataNilai',
    'olahDataRPS',
    'presensiKuliah',
    'rekapHasilKuliah',
    'rekapKRS',
    'rekapPresensi',
    'rekapRPS',
    'subPokokBahasan',
    'tinymce',
    'qr_code',
    # 'import_export',
    # 'reports'
    
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

ROOT_URLCONF = 'simprosis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'simprosis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # Using sqlite3
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : 'simprosis',
        'USER'      : 'root',
        'PASSWORD'  : '',
        'HOST'      : 'localhost',
        'PORT'      : '3306'
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]


TINYMCE_JS_URL = os.path.join(STATIC_URL, 'vendor/tinymce/js/tinymce/tinymce.min.js')
TINYMCE_JS_ROOT = os.path.join(STATIC_URL, 'vendor/tinymce/js/tinymce')

TINYMCE_DEFAULT_CONFIG = {
    'height' : 300,
    'plugins': "image,imagetools,media,codesample,link,code",
    'cleanup_on_startup': True,
    'menubar': False,
    'toolbar': "styleselect |undo redo | bold italic | alignleft aligncenter alignright | link image media codesample code",
    'image_caption': True,
    'image_advtab': True,
    'custom_undo_redo_levels': 10,
    'file_browser_callback' : "myFileBrowser"
}


# Caches.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'qr-code': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'qr-code-cache',
        'TIMEOUT': 3600
    }
}

# Django QR Code specific options.
QR_CODE_CACHE_ALIAS = 'qr-code'
QR_CODE_URL_PROTECTION = {
    constants.TOKEN_LENGTH: 30,  # Optional random token length for URL protection. Defaults to 20.
    constants.SIGNING_KEY: 'my-secret-signing-key',  # Optional signing key for URL token. Uses SECRET_KEY if not defined.
    constants.SIGNING_SALT: 'my-signing-salt',  # Optional signing salt for URL token.
    constants.ALLOWS_EXTERNAL_REQUESTS_FOR_REGISTERED_USER: False   # Tells whether a registered user can request the QR code URLs from outside a site that uses this app. It can be a boolean value used for any user, or a callable that takes a user as parameter. Defaults to False (nobody can access the URL without the security token).
}

# import export 
# IMPORT_EXPORT_USE_TRANSACTIONS = True
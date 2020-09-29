"""
Django settings for blogp1e0 project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qp6(y1!uc10!+n)unb%fs=b3g#q2u%skwmmvr33&hfedssr^!v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'news.apps.NewsConfig',
    'voicea.apps.VoiceaConfig',
    'crispy_forms',
    'taggit',
    'social_django',
    'sslserver',
    'rest_framework',
    'rest_framework.authtoken',
    # 'social.apps.django_app.default',
    # 'easy_thumbnails',
    # 'send_email.apps.SendEmailConfig',
    # 'captcha',
    # 'django.contrib.humanize'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'blogp1e0.urls'

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

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',  # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'blogp1e0.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# MIGRATION_MODULES = {
#     'newsapp': 'testpackage.migrations.news'
# }

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'


#USE_I18N = True

TIME_ZONE = 'UTC'

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '../diploma/static',
)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# RECAPTCHA_PUBLIC_KEY  =  '6Le3l7AZAAAAAL0IIKH_1eS83nqe9TzO_amN8OD-'
# RECAPTCHA_PRIVATE_KEY =  '6Le3l7AZAAAAAHbDevZstQbCg968r3GYiVE3XSwW'


# social auth
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_GITHUB_KEY = 'fda822d3a434a36e4fc1'
SOCIAL_AUTH_GITHUB_SECRET = '5be6bf6973b69df4edd654453584fc539e2bd283'

SOCIAL_AUTH_FACEBOOK_KEY = '1267032736974613'
SOCIAL_AUTH_FACEBOOK_SECRET = '2a87d50ff5bc33f9faa2e988f4685056'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''  # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''  # Google Consumer Secret

SOCIAL_AUTH_TWITTER_KEY = 'xnKe4EUS6FZjkMoPnlOjdf34G'
SOCIAL_AUTH_TWITTER_SECRET = 'vNC32nJQLiCQ0EJrviEJRTx0PKjYL3pgNjTbR4f103RibXlEPl'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'djangoprblog@gmail.com'
EMAIL_HOST_PASSWORD = 'MK7fe188'

# Multilingualism

USE_I18N = True

LOCALE_PATHS = (
    'locale',
    # os.path.join(PROJECT_DIR, 'locale'),
)

LANGUAGE_CODE = 'en'  # язык сайта по умолчанию

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)
"""
Django settings for djangoresume project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os 

import sys
RUNNING_DEVSERVER = (len(sys.argv) > 1 and sys.argv[1] == 'runserver')
print("RUNNING_DEVSERVER: "+str(RUNNING_DEVSERVER))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#Deploy settings
#SECURE_CONTENT_TYPE_NOSNIFF = True     #Not needed because Django isn’t involved in serving user-uploaded files
#SECURE_BROWSER_XSS_FILTER = True    #Protection
#SECURE_SSL_REDIRECT = True          #Serve https
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
print("BASE_DIR: "+str(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if os.environ.get('SECRET_KEY') is None:
    print('')
    import sys
    sys.exit("Please define an environment variable as follows:\nexport SECRET_KEY='some text'")

SECRET_KEY=os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = RUNNING_DEVSERVER
print("DEBUG: "+str(DEBUG))

ALLOWED_HOSTS = ['127.0.0.1','aless80.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "compressor",
    'resume'
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

ROOT_URLCONF = 'djangoresume.urls'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'resume/templates')]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
              'django.template.context_processors.media', #TO USE MEDIA_URL
            ],
        },
    },
]

LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'djangoresume.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, '/static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, "resume/")
MEDIA_URL = '/'

print("STATIC_ROOT: "+str(STATIC_ROOT))
print("STATIC_URL: "+str(STATIC_URL))
print("STATICFILES_DIRS: "+str(STATICFILES_DIRS))
print("")

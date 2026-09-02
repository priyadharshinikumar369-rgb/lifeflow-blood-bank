"""
Django settings for config project.
"""

from pathlib import Path

# ================= BASE DIRECTORY =================

BASE_DIR = Path(__file__).resolve().parent.parent

# ================= SECURITY =================

SECRET_KEY = 'django-insecure-5eupnu#_3owp1&ruo2*f=*6+bewmo6d=3am4fc9c@7-^ilr%t1'

DEBUG = True

ALLOWED_HOSTS = ['lifeflow-blood-bank-16.onrender.com']

# ================= APPLICATIONS =================

INSTALLED_APPS = [
# Django Apps
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',

# Local Apps
'home',
'accounts',
'donor',
'patient',
'inventory',
'dashboard',
'appointments',
'reports',
'news',
'contact',

]

# ================= MIDDLEWARE =================

MIDDLEWARE = [
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ================= URL CONFIGURATION =================

ROOT_URLCONF = 'config.urls'

# ================= TEMPLATES =================

TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        BASE_DIR / 'templates',
    ],

    'APP_DIRS': True,

    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
},
]

# ================= WSGI =================

WSGI_APPLICATION = 'config.wsgi.application'

# ================= DATABASE =================

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}

# ================= PASSWORD VALIDATION =================

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

# ================= INTERNATIONALIZATION =================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# ================= STATIC FILES =================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# ================= MEDIA FILES =================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# ================= LOGIN / LOGOUT =================

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

# ================= DEFAULT PRIMARY KEY =================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

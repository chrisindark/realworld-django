from conduit.settings.common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2^f+3@v7$v1f8yt0!s)3-1t$)tlp+xm17=*g))_xoi&&9m#2a&'

ALLOWED_HOSTS = (
    'localhost',
    '127.0.0.1',
)

INSTALLED_APPS += (
    'django_extensions',
    'rest_framework_swagger',
)

LOGIN_URL = '/api-auth/login/'
LOGOUT_URL = '/api-auth/logout/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
    'rest_framework.authentication.SessionAuthentication',
    'conduit.apps.authentication.backends.JWTAuthentication',
)

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        },
        'permission_denied_handler': 'django.contrib.auth.views.login',
        'is_authenticated': True,  # Set to True to enforce user authentication,
        'is_superuser': True  # Set to True to enforce admin only access
    }
}

# DATABASE SETTINGS
DATABASES = {
    'default': {
        'NAME': 'realworld_django',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'mindfire',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

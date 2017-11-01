from conduit.settings.common import *
import dj_database_url

DEBUG = True

SECRET_KEY = get_env_var('SECRET_KEY')

ALLOWED_HOSTS = (
    'salty-ridge-21622.herokuapp.com',
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

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

CORS_ORIGIN_WHITELIST = ()

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

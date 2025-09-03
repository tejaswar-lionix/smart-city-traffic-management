import os, sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'smart-city-dev-secret-key-2025')
DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'
ALLOWED_HOSTS = ['*']
USE_SQLITE = os.environ.get('USE_SQLITE', '1') == '1'
INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'rest_framework','corsheaders',
    'apps.traffic_signals',
        'apps.intersections',
        'apps.sensors',
        'apps.vehicles',
        'apps.incidents',
        'apps.congestion',
        'apps.parking',
        'apps.public_transit',
        'apps.pedestrian',
        'apps.cycling',
        'apps.emissions',
        'apps.road_network',
        'apps.enforcement',
        'apps.weather',
        'apps.energy',
        'apps.fleet_management',
        'apps.analytics',
        'apps.user_management',
]
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','corsheaders.middleware.CorsMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware']
ROOT_URLCONF = 'smart_city.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'smart_city.wsgi.application'
if USE_SQLITE:
    DATABASES = {'default': {'ENGINE':'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3'}}
else:
    DATABASES = {'default': {'ENGINE':'django.db.backends.postgresql','NAME': os.environ.get('POSTGRES_DB','smart_city'),'USER': os.environ.get('POSTGRES_USER','postgres'),'PASSWORD': os.environ.get('POSTGRES_PASSWORD','postgres'),'HOST': os.environ.get('POSTGRES_HOST','db'),'PORT': os.environ.get('POSTGRES_PORT','5432')}}
CACHES = {'default': {'BACKEND':'django.core.cache.backends.redis.RedisCache','LOCATION': os.environ.get('REDIS_URL','redis://redis:6379/0')}} if not USE_SQLITE else {'default': {'BACKEND':'django.core.cache.backends.locmem.LocMemCache'}}
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL','redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND','redis://redis:6379/0')
LANGUAGE_CODE='en-us'; TIME_ZONE='UTC'; USE_TZ=True; STATIC_URL='static/'; DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
REST_FRAMEWORK={'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.AllowAny'],'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination','PAGE_SIZE':20}
CORS_ALLOW_ALL_ORIGINS=True
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','smart_city.settings')
import django
try: django.setup()
except: pass

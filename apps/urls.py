from django.urls import path, include
urlpatterns = []
# per-app urls included via main router
try:
    from django.urls import re_path
except: pass

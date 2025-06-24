from django.urls import path, include
from django.http import JsonResponse
def health(request): return JsonResponse({'status':'ok','city':'smart-traffic'})
urlpatterns = [path('health/', health), path('api/', include('apps.urls'))]

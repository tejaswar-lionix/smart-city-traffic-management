from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import WeatherService
from .serializers import WeatherSerializer
class WeatherListView(APIView):
    def get(self, request):
        svc = WeatherService(config={})
        data = svc.process_weather_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = WeatherSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = WeatherService(config={})
        res = svc.process_weather_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

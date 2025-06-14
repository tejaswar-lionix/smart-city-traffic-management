from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import SensorsService
from .serializers import SensorsSerializer
class SensorsListView(APIView):
    def get(self, request):
        svc = SensorsService(config={})
        data = svc.process_sensors_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = SensorsSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = SensorsService(config={})
        res = svc.process_sensors_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

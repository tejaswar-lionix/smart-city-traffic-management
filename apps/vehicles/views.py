from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import VehiclesService
from .serializers import VehiclesSerializer
class VehiclesListView(APIView):
    def get(self, request):
        svc = VehiclesService(config={})
        data = svc.process_vehicles_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = VehiclesSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = VehiclesService(config={})
        res = svc.process_vehicles_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

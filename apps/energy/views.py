from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import EnergyService
from .serializers import EnergySerializer
class EnergyListView(APIView):
    def get(self, request):
        svc = EnergyService(config={})
        data = svc.process_energy_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = EnergySerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = EnergyService(config={})
        res = svc.process_energy_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
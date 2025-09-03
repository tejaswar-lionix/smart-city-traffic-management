from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import FleetManagementService
from .serializers import FleetManagementSerializer
class FleetManagementListView(APIView):
    def get(self, request):
        svc = FleetManagementService(config={})
        data = svc.process_fleet_management_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = FleetManagementSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = FleetManagementService(config={})
        res = svc.process_fleet_management_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
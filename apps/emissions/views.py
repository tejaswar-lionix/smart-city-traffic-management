from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import EmissionsService
from .serializers import EmissionsSerializer
class EmissionsListView(APIView):
    def get(self, request):
        svc = EmissionsService(config={})
        data = svc.process_emissions_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = EmissionsSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = EmissionsService(config={})
        res = svc.process_emissions_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import IncidentsService
from .serializers import IncidentsSerializer
class IncidentsListView(APIView):
    def get(self, request):
        svc = IncidentsService(config={})
        data = svc.process_incidents_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = IncidentsSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = IncidentsService(config={})
        res = svc.process_incidents_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

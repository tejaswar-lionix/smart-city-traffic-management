from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import CyclingService
from .serializers import CyclingSerializer
class CyclingListView(APIView):
    def get(self, request):
        svc = CyclingService(config={})
        data = svc.process_cycling_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = CyclingSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = CyclingService(config={})
        res = svc.process_cycling_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
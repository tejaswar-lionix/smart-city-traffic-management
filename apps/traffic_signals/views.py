from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import TrafficSignalsService
from .serializers import TrafficSignalsSerializer
class TrafficSignalsListView(APIView):
    def get(self, request):
        svc = TrafficSignalsService(config={})
        data = svc.process_traffic_signals_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = TrafficSignalsSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = TrafficSignalsService(config={})
        res = svc.process_traffic_signals_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
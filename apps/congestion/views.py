from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import CongestionService
from .serializers import CongestionSerializer
class CongestionListView(APIView):
    def get(self, request):
        svc = CongestionService(config={})
        data = svc.process_congestion_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = CongestionSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = CongestionService(config={})
        res = svc.process_congestion_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

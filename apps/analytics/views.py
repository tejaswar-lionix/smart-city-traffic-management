from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import AnalyticsService
from .serializers import AnalyticsSerializer
class AnalyticsListView(APIView):
    def get(self, request):
        svc = AnalyticsService(config={})
        data = svc.process_analytics_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = AnalyticsSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = AnalyticsService(config={})
        res = svc.process_analytics_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
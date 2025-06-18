from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import PublicTransitService
from .serializers import PublicTransitSerializer
class PublicTransitListView(APIView):
    def get(self, request):
        svc = PublicTransitService(config={})
        data = svc.process_public_transit_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = PublicTransitSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = PublicTransitService(config={})
        res = svc.process_public_transit_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

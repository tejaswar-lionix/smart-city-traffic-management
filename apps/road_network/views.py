from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import RoadNetworkService
from .serializers import RoadNetworkSerializer
class RoadNetworkListView(APIView):
    def get(self, request):
        svc = RoadNetworkService(config={})
        data = svc.process_road_network_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = RoadNetworkSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = RoadNetworkService(config={})
        res = svc.process_road_network_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
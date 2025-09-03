from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import PedestrianService
from .serializers import PedestrianSerializer
class PedestrianListView(APIView):
    def get(self, request):
        svc = PedestrianService(config={})
        data = svc.process_pedestrian_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = PedestrianSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = PedestrianService(config={})
        res = svc.process_pedestrian_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import ParkingService
from .serializers import ParkingSerializer
class ParkingListView(APIView):
    def get(self, request):
        svc = ParkingService(config={})
        data = svc.process_parking_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = ParkingSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = ParkingService(config={})
        res = svc.process_parking_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

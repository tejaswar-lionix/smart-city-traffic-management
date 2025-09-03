from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import IntersectionsService
from .serializers import IntersectionsSerializer
class IntersectionsListView(APIView):
    def get(self, request):
        svc = IntersectionsService(config={})
        data = svc.process_intersections_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = IntersectionsSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = IntersectionsService(config={})
        res = svc.process_intersections_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
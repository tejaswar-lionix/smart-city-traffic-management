from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import EnforcementService
from .serializers import EnforcementSerializer
class EnforcementListView(APIView):
    def get(self, request):
        svc = EnforcementService(config={})
        data = svc.process_enforcement_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = EnforcementSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = EnforcementService(config={})
        res = svc.process_enforcement_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)

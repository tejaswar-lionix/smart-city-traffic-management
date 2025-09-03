from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import UserManagementService
from .serializers import UserManagementSerializer
class UserManagementListView(APIView):
    def get(self, request):
        svc = UserManagementService(config={})
        data = svc.process_user_management_0({'value':10}, {})
        return Response(data)
    def post(self, request):
        ser = UserManagementSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        svc = UserManagementService(config={})
        res = svc.process_user_management_1(request.data)
        return Response(res, status=status.HTTP_201_CREATED)
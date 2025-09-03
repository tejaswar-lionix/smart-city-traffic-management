from django.urls import path
from .views import UserManagementListView
urlpatterns = [path('user_management/', UserManagementListView.as_view())]
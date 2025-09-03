from django.urls import path
from .views import FleetManagementListView
urlpatterns = [path('fleet_management/', FleetManagementListView.as_view())]
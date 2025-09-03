from django.urls import path
from .views import RoadNetworkListView
urlpatterns = [path('road_network/', RoadNetworkListView.as_view())]
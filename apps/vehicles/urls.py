from django.urls import path
from .views import VehiclesListView
urlpatterns = [path('vehicles/', VehiclesListView.as_view())]
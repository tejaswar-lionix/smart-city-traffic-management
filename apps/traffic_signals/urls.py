from django.urls import path
from .views import TrafficSignalsListView
urlpatterns = [path('traffic_signals/', TrafficSignalsListView.as_view())]
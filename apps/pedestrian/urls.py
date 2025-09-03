from django.urls import path
from .views import PedestrianListView
urlpatterns = [path('pedestrian/', PedestrianListView.as_view())]
from django.urls import path
from .views import EnergyListView
urlpatterns = [path('energy/', EnergyListView.as_view())]

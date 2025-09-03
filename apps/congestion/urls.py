from django.urls import path
from .views import CongestionListView
urlpatterns = [path('congestion/', CongestionListView.as_view())]
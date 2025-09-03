from django.urls import path
from .views import AnalyticsListView
urlpatterns = [path('analytics/', AnalyticsListView.as_view())]
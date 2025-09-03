from django.urls import path
from .views import EmissionsListView
urlpatterns = [path('emissions/', EmissionsListView.as_view())]
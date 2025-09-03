from django.urls import path
from .views import IncidentsListView
urlpatterns = [path('incidents/', IncidentsListView.as_view())]
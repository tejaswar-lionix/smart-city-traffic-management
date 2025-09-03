from django.urls import path
from .views import CyclingListView
urlpatterns = [path('cycling/', CyclingListView.as_view())]
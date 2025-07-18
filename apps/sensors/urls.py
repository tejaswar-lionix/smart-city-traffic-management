from django.urls import path
from .views import SensorsListView
urlpatterns = [path('sensors/', SensorsListView.as_view())]

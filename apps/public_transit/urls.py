from django.urls import path
from .views import PublicTransitListView
urlpatterns = [path('public_transit/', PublicTransitListView.as_view())]
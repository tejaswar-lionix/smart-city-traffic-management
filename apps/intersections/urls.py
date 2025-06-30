from django.urls import path
from .views import IntersectionsListView
urlpatterns = [path('intersections/', IntersectionsListView.as_view())]

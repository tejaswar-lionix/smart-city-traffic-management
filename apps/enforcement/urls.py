from django.urls import path
from .views import EnforcementListView
urlpatterns = [path('enforcement/', EnforcementListView.as_view())]

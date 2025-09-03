from django.apps import AppConfig
class RoadNetworkConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name='apps.road_network'
    verbose_name='Graph routing Dijkstra A*, BPR cost, OD matrix'
from django.apps import AppConfig
class PublicTransitConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name='apps.public_transit'
    verbose_name='Buses, GTFS, headway adherence, dwell, TSP'

from django.apps import AppConfig
class CongestionConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name='apps.congestion'
    verbose_name='BPR, TTI, buffer index, LOS, queue, shockwave, bottleneck'
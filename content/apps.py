from django.apps import AppConfig
from .scheduler import tasks

class ContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content'
    
    
    def ready(self):
        tasks.start()

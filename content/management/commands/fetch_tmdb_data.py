from typing import Any
from django.core.management.base import BaseCommand
from core.v2.views import fetch_tmdb_data

class Command(BaseCommand):
    help = 'Fetch genres from TMDB and update the database'
    
    def handle(self, *args, **options):
        try:
            fetch_tmdb_data()
            self.stdout.write(self.style.SUCCESS("Successfully updated genres from TMDB"))
        except:
            self.stderr.write(self.style.ERROR("Fetch data and update failed."))
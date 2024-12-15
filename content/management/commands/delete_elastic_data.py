from django.core.management.base import BaseCommand
from elasticsearch_dsl import connections, Index
from decouple import config


# Connect to Elasticsearch
ELASTIC_SEARCH_HOST = config("ELASTIC_SEARCH_HOST")
connections.create_connection(hosts=[ELASTIC_SEARCH_HOST])

class Command(BaseCommand): 
    help = "Deletes the specified index in ElasticSearch"
    
    def add_arguments(self, parser):
        # Add an argument for the index name
        parser.add_argument(
            'index_name', 
            type=str, 
            help='The name of the Elasticsearch index to delete'
        )
    
    def handle(self, *args, **kwargs):
        # Specify the index name
        index_name = kwargs["index_name"]
        # Access the index
        index = Index(index_name)
        # Check if the index exists
        if index.exists():
            # Delete the index
            index.delete()
            self.stdout.write(self.style.SUCCESS(f"Index {index_name} Successfully Deleted!"))
        else:
            self.stdout.write(self.style.WARNING(f"Index {index_name} does not exist."))
            
    
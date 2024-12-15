from elasticsearch_dsl import Index, Document, connections
from content.models import Content
from decouple import config

ELASTIC_SEARCH_HOST = config("ELASTIC_SEARCH_HOST")
connections.create_connection(hosts=[ELASTIC_SEARCH_HOST])

# define the index in ElasticSearch
content_index = Index("content")

# define the document
class ContentDocument(Document):
    class Index:
        # name of the ElasticSearch index, defined upper
        name = "content"
        
    class Django:
        model = Content # the model to index
        fields = [
            "title",  # Fields from the model you want to search by
            "description",
            "category",
            "release_date",
        ]
        
    


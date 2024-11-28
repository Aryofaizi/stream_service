from elasticsearch_dsl import Index, Document
from content.models import Content

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
        ]
        
    


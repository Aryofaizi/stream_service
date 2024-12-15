from django.dispatch import receiver
from django.db.models.signals import post_save
from content.models import Content
from .documents import ContentDocument

# handle create/update events
@receiver(post_save, sender=Content)
def index_content_to_elasticsearch(sender, instance, **kwargs):
    # index or update document in ElasticSearch
    content_document = ContentDocument(
        meta={"id": instance.id}, # Use MySQL primary key as document ID
        title=instance.title,
        description=instance.description,
        category=instance.category,
        release_date=instance.release_date,
    )
    content_document.save()
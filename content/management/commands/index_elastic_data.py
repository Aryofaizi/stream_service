from django.core.management.base import BaseCommand
from content.v2.documents import ContentDocument
from content.models import Content

class Command(BaseCommand):
    help = "Index all MyModel objects into Elasticsearch"
    
    def handle(self, *args, **kwargs):
        for obj in Content.objects.all():
            doc = ContentDocument(
                meta={"id":obj.id},
                title=obj.title,
                description=obj.description,
                category=obj.category,
                release_date=obj.release_date,
                )
            doc.save()
        self.stdout.write(self.style.SUCCESS("Successfully indexed all objects"))
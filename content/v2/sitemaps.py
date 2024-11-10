# sitemaps
from django.contrib.sitemaps import Sitemap
from content.models import Content


class ContentSitemap(Sitemap):
    changefreq = "weekly"  # How often this content changes
    priority = 0.8  # Priority (0.0 to 1.0) for search engines
    
    
    def items(self):
        return Content.objects.all()  # All movies in your database
    
    def lastmod(self, obj):
        return obj.datetime_modified  # Use the last update date of each content
    
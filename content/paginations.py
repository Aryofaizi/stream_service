from rest_framework.pagination import PageNumberPagination

class ContentPagination(PageNumberPagination):
    """Sets a custom pagination for content List endpoint."""
    page_size = 30
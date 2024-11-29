from .documents import ContentDocument
from django.http import JsonResponse


def search_content(request):
    """seach functionality with ElasticSearch Engine."""
    query = request.GET.get("q", '') # Get the search query from the URL
    if not query :
        return JsonResponse({"error": "please enter a search term"}, status=400)
    
    # search for the query
    search = ContentDocument.search().query("fuzzy", title=query)
    results = search.execute()
    
    #return search results as json
    return JsonResponse([hit.to_dict() for hit in results], safe=False) # safe false because we want to return as list
    
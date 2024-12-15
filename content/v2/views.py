from .documents import ContentDocument
from django.http import JsonResponse


def search_content(request):
    """seach functionality with ElasticSearch Engine."""
    query = request.GET.get("q", '') # Get the search query from the URL
    category = request.GET.get("category", None)  # Example filter: category
    release_date = request.GET.get("year", None)  # Example filter: release year
    page = int(request.GET.get("page", 1)) # Pagination: default to page 1
    PER_PAGE = 10 # Number of results per page
    if not query :
        return JsonResponse({"error": "please enter a search term"}, status=400)
    
    # Apply search query
    search = ContentDocument.search().query(
        "multi_match", query=query, fields=["title", "description"]
        )
    # Aplly filters 
    if category: 
        search = search.filter("term", category=category)
    if release_date:
        search = search.filter("term", release_date=release_date)

    # Apply pagination
    start = (page-1) * PER_PAGE
    end = start + PER_PAGE
    results = search[start:end].execute()
    
    # Format the response
    response = {
        "total": results.hits.total.value,
        "page": page,
        "per_page" : PER_PAGE,
        "results" : [hit.to_dict() for hit in results]
    }
    
    #return search results as json
    return JsonResponse(response)
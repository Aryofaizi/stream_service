#core v2
import requests
from decouple import config
import logging
from django.http import HttpResponse

TMDB_TOKEN = config("TMDB_TOKEN")

def fetch_tmdb_data():
    """Get TMDB data"""
    # Set up logging to print or save logs for debugging
    # Importing Genre inside the function ensures lazy loading
    from content.models import Genre  # Importing inside the function to avoid issues
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Fetching TMDB data...")  # Log that the function is being called

    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    genres = response.json().get("genres", [])
    new_genres = [
        Genre(tmdb_id=genre["id"], title=genre["name"])
        for genre in genres
    ]
    
    # Bulk create the genres (avoiding conflicts)
    Genre.objects.bulk_create(new_genres, ignore_conflicts=True)

    logger.info(f"Created {len(new_genres)} genres.")
    
    
    
def populate_content_table(request):
    """fetch tmdb movies and populate content table in database."""
    # Importing class inside the function ensures lazy loading
    from content.models import Content,Genre

    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    contents = response.json().get("results", [])
    new_contents = []
    # Cache existing genres so that we can use instance in establishing many to many relationships
    genre_map = {g.tmdb_id: g for g in Genre.objects.all()}
    
    for content in contents:
        new_contents.append(Content(
            tmdb_id=content["id"],
            title=content["title"],
            description=content["overview"],
            release_date=content["release_date"],
        ))
    
    # bulk create contents
    Content.objects.bulk_create(new_contents, ignore_conflicts=True)
    # Establish many-to-many relationships
    content_in_db = {content.tmdb_id: content for content in Content.objects.all()}
    for item in contents:
        content = content_in_db.get(item["id"])  
        if content:
            genre_ids = item.get("genre_ids", [])
            content.genre.add(*[genre_map[genre] for genre in genre_ids])
    
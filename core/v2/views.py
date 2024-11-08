#core v2
import requests
from decouple import config
import logging

def fetch_tmdb_data():
    """Get TMDB data"""
    # Set up logging to print or save logs for debugging
    # Importing Genre inside the function ensures lazy loading
    from content.models import Genre  # Importing inside the function to avoid issues
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Fetching TMDB data...")  # Log that the function is being called

    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    TMDB_TOKEN = config("TMDB_TOKEN")
    
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
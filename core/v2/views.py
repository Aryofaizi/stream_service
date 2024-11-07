#core v2
import requests
from content.models import Genre
from decouple import config


def fetch_tmdb_data():
    """get tmdb data"""
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
    #bulk create the genres
    Genre.objects.bulk_create(new_genres, ignore_conflicts=True)





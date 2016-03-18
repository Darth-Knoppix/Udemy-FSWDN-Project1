# Seth Corker 2016

import media
import fresh_tomatoes
import urllib.request
import json

# Get the description and rating from omdbapi.com via JSON
def scrape_movie(name, video):
    url = "http://www.omdbapi.com/?t=" + name.replace(" ", "+")
    with urllib.request.urlopen(url) as response:
       html = response.read().decode('utf-8')
       data = json.loads(html)
       return media.Movie(  data['Title'], data['Poster'],video,
                            data["Plot"], data['imdbRating'])

# List of movies to be displayed
movies = [
    scrape_movie("Fight Club", "J8FRBYOFu2w"),
    scrape_movie("Schindler's List", "dwfIf1WMhgc"),
    scrape_movie("The Dark Knight", "EXeTwQWrcwY"),
    scrape_movie("Shawshank Redemption", "6hB3S9bIaco")
]

# Generate the page
fresh_tomatoes.open_movies_page(movies)

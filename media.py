# Seth Corker 2016

# Holds information about a movie
class Movie:
    global title
    global poster_image_url
    global trailer_youtube_url
    global description
    global rating

    def __init__(self, title, box_art_url, yurl, plot, rating):
        self.title = title
        self.poster_image_url = box_art_url
        self.trailer_youtube_url = "https://www.youtube.com/watch?v=" + yurl
        self.description = plot
        self.rating = rating

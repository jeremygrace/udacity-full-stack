import webbrowser


class Movie ():
    """This class provides a way to store movie related information."""
    def __init__(self, movie_title, movie_actors, movie_genre,
                         movie_storyline, poster_image, trailer_youtube):
        """Initalize the instance variables"""
        self.title = movie_title
        self.actors = movie_actors
        self.genre = movie_genre
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
        

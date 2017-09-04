# Movie Trailer Python - Udaciy Fullstack Nanodegree assignment
Using python to create a website to post movies, also you can watch the movie trailers.

## Requirements

- Modify the entertainment_center.py file to include movies that you want to display
- run python entertainment_center.py
- it should generate a fresh_tomatoes.html file which will open in a browser

## Technologies Used
- Pyhton
- Bootstrap
- Objects
- Classes

## Code Explaination
- The code in this repo creates and HTML file based on an array of instantiated objects
- The fresh_tomatoes.py was starter code from Udacity, it takes and array of movies and created div containers for each move
- Each container is styled and put together using the different parts of the object
- below is a class that I wrote based on my notes from the nanodegree

```
import webbrowser

class Movie():
	VALID_RATINGS = ['G', 'PG', 'GP-13', 'R']

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

```
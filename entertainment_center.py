import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
						'A story of a boy and his toys that come to life',
						'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 
						'https://www.youtube.com/watch?v=vwyZH85NQC4')

# print(toy_story.storyline)
avatar = media.Movie('Avatar',
					 'A marine on an alien planet',
					 'http://upload.wikimedia.org/wikimedia/id/b/b0/Avatar-Teaser-Poster.jpg',
					 'http://www.youtube.com/watch?v=-9ceBgWV890')

aeon_flux = media.Movie('Aeon Flux', 
						'Aeon Flux is a mysterious and amoral secret agent from the country of Monica Her. motives or background are left unexplained, as are those of her antagonist/love, Trevor Goodchild',
						'https://images-na.ssl-images-amazon.com/images/M/MV5BOWFlYzc1NDAtMjhkYi00OGRkLWExYTAtODQ3MzE1MGU1MTY5XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR6,0,182,268_AL_.jpg',
						'https://www.youtube.com/watch?v=CTf1rKI1rLI')

ex_machina = media.Movie('Ex Machina', 
						 'A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.',
						 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
						 'https://www.youtube.com/watch?v=bggUmgeMCdc')

movies = [toy_story, avatar, aeon_flux, ex_machina] 


fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.__doc__)
# print('name of class: ' + media.Movie.__name__)
# print('module name: ' + media.Movie.__module__)



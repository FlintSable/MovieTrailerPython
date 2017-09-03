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

movies = [toy_story, avatar, aeon_flux] 

print(media.Movie.__doc__)
print('name of class: ' + media.Movie.__name__)
print('module name: ' + media.Movie.__module__)



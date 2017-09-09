# importing a class and a helper module from these files
import media
import fresh_tomatoes

ghost_in_the_shell = media.Movie('Ghost in the Shell',
						'In the near future, Major is the first of her kind: A human saved from a terrible crash',
						'https://images-na.ssl-images-amazon.com/images/M/MV5BM2FhYzVkMzQtOTVlYS00NTYxLThjNzktMDVhNjU1MDE0ZTc5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,701,1000_AL_.jpg', 
						'https://www.youtube.com/watch?v=0j6wsGuzP2Q')

# print(toy_story.storyline)
gundam_wing = media.Movie('Gundam Wing',
					 'Treize Kushrenada is dead and the 5 young soldiers known as the Gundam pilots have brought peace between Earth and the Colonies through Operation me.',
					 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NzQ3MDA0M15BMl5BanBnXkFtZTcwMjk0NTE0MQ@@._V1_.jpg',
					 'https://www.youtube.com/watch?v=90REc5yGl40')

aeon_flux = media.Movie('Aeon Flux', 
						'Aeon Flux is a mysterious and amoral secret agent from the country of Monica Her. motives or background are left unexplained, as are those of her antagonist/love, Trevor Goodchild',
						'https://images-na.ssl-images-amazon.com/images/M/MV5BOWFlYzc1NDAtMjhkYi00OGRkLWExYTAtODQ3MzE1MGU1MTY5XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR6,0,182,268_AL_.jpg',
						'https://www.youtube.com/watch?v=CTf1rKI1rLI')

ex_machina = media.Movie('Ex Machina', 
						 'A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.',
						 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_UX182_CR0,0,182,268_AL_.jpg',
						 'https://www.youtube.com/watch?v=bggUmgeMCdc')

alien_resurrection = media.Movie('Alien: Resurrection',
								 'Two centuries after her death, Ellen Ripley is revived as a powerful human/alien hybrid clone who must continue her war against the aliens.',
								 'https://images-na.ssl-images-amazon.com/images/M/MV5BM2YxYmFjYWMtMzBmMC00MTVmLThhMjUtYWU5Yzg2OGQwZjE3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg',
								 'https://www.youtube.com/watch?v=4ZzRFT3k7Q4')

movies = [ghost_in_the_shell, gundam_wing, aeon_flux, ex_machina, alien_resurrection] 


fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.__doc__)
# print('name of class: ' + media.Movie.__name__)
# print('module name: ' + media.Movie.__module__)



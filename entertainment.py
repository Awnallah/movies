import fresh_tomatoes
import media
import csv

# toy_story = media.Movie("Toy Story",
#  						'A story of a boy and his toys that came to life',
#  						'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
#  						'https://www.youtube.com/watch?v=KYz2wyBy3kc')

# #print(toy_story.storyline)

# avatar = media.Movie('Avatar',
# 					'A marine on an alien planet',
# 					'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
# 					'https://www.youtube.com/watch?v=5PSNL1qE6VY')
# #avatar.show_trailer()
# #print(avatar.storyline)
# #toy_story.show_trailer()

def pull_movies(file):
    """ pulls movie data from excel and returns a list of Movie objects """
    movies = []
    with open(file, 'rb') as csvfile:
        movie_table = csv.DictReader(csvfile)
        for movie in movie_table:
            movies.append(media.Movie(movie_title=movie['movie_title'],
                                poster_image=movie['poster_image'],
                                trailer_youtube=movie['trailer_youtube']))
    return movies



movies = pull_movies('movieData/movieData.csv')
fresh_tomatoes.open_movies_page(movies)
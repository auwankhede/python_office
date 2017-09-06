import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=hxGB7LU4i1I")



avator = media.Movie("Avator",
                     "Science fixtion alian move",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=3qrlNXpSeEU")


matrix = media.Movie("The Matrix",
                     " It depicts a dystopian future in which reality as perceived by most humans is actually a simulated reality called matrix created by sentient machines to subdue the human population, while their bodies' heat and electrical activity are used as an energy source. ",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=ccQPesc7HFs"
                     
                     )
print(matrix.title)
matrix.show_trailer();
#list_movies = [toy_story, avator, matrix]
#fresh_tomatoes.open_movies_page(list_movies)
#print(media.Movie.VALID_RATINGS)


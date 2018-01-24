import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https:\\www.youtube.com\\watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)
heat = media.Movie("Heat",
                     "A crime film involving Neil McCauley who was planning his last heist before retirement",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Heatposter.jpg/220px-Heatposter.jpg",
                     "https://www.youtube.com/watch?v=0xbBLJ1WGwQ")

#  print(avatar.storyline)

The_Foreigner = media.Movie("The Foreigner",
                     "An action thriller featuring Jackie Chan",
                     "https://en.wikipedia.org/wiki/The_Foreigner_(2017_film)",
                     "https://www.youtube.com/watch?v=EypTSjHoFsg")


# print(The_Foreigner.storyline)
# The_Foreigner.show_trailer()                     
school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris", "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

eagle_eye = media.Movie("Eagle Eye", "Jerry and Rachel's lives were disrupted by a stranger they never met. As their lives became imperiled, they had to figure out why before it is too late.",
                                "https://images-na.ssl-images-amazon.com/images/I/51wWFFfTIsL.jpg",
                                "https://www.youtube.com/watch?v=olRdPXwiSjk")

point_break = media.Movie("Point Break", "A thriller movie involving Utah who makes friends with a group of thieves who steal money to give to the poor",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNWVjZWFmYjItZGJlOC00YTllLWE4YjctMWY2ZTg5ZjE0MDIyXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                           "https://www.youtube.com/watch?v=ncvFAm4kYCo")

movies = [toy_story, heat, school_of_rock, ratatouille, eagle_eye, point_break]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.valid_ratings)
#  print(media.Movie.__doc__)


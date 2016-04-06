import fresh_tomatoes
import media

# IMDb's movie descriptions were used to craft storylines.
# Links from IMDb and YouTube were utilized.
"""Import media to connect media.Movie info"""
"""Import fresh_tomatoes to generate HTML file"""

interstellar = media.Movie(
                    "Interstellar",
                    "Matthew McConaughey, Anne Hathaway,\
                    and Michael Caine",
                    "Sci-Fi",
                    "A team of space explorers travel through \
                    a wormhole in space in a last-ditch \
                    effort to ensure humanity's survival.",
                    "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg",   # noqa
                    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

good_will_hunt = media.Movie(
                    "Good Will Hunting",
                    "Matt Damon, Robin Williams, \
                    and Ben Affleck",
                    "Drama",
                    "A janitor at M.I.T. has a gift for mathematics, \
                    but lacks direction in his life. \
                    A psychologist is asked to help and \
                    they both enter a journey of \
                    conflict and deep reflection.",
                    "http://ia.media-imdb.com/images/M/MV5BMTk0NjY0Mzg5MF5BMl5BanBnXkFtZTcwNzM1OTM2MQ@@._V1_SY317_CR1,0,214,317_AL_.jpg",   # noqa
                    "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

star_wars = media.Movie(
                    "Star Wars: The Force Awakens",
                    "Mark Hamill, Harrison Ford, \
                    and Carrie Fisher",
                    "Adventure",
                    "The Saga continues, set thirty years \
                    after Episode VI - Return of the Jedi",
                    "http://ia.media-imdb.com/images/M/MV5BMjEwMDg4NjIyMl5BMl5BanBnXkFtZTgwNTQzNTc2NjE@._V1_SX214_AL_.jpg",   # noqa
                    "https://www.youtube.com/watch?v=ngElkyQ6Rhs")
hunger_games = media.Movie(
                    "The Hunger Games: Mockingjay Part 2",
                    "Jennifer Lawrence, Josh Hutcherson, \
                    and Liam Hemsworth",
                    "Adventure",
                    "The Final Chapter begins. Katiness Everdeen \
                    leads a revolution against the autocratic Capitol.",
                    "http://ia.media-imdb.com/images/M/MV5BMzg4OTcxNzAyNV5BMl5BanBnXkFtZTgwOTc4MTEyNjE@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
                    "https://www.youtube.com/watch?v=n-7K_OjsDCQ")

elf = media.Movie(
                    "Elf",
                    "Will Ferrell, James Caan, \
                    and Zooey Deschanel",
                    "Comedy",
                    "Buddy (Will Ferrell), a human elf, \
                    ventures to New York City in search \
                    of his true identity.",
                    "http://ia.media-imdb.com/images/M/MV5BNjY1NjQ3NDY5MF5BMl5BanBnXkFtZTYwODAyMTc3._V1_SX214_AL_.jpg",   # noqa
                    "https://www.youtube.com/watch?v=gW9wRNqQ_P8")

no_reservations = media.Movie(
                    "No Reservations",
                    "Catherine Zeta-Jones, Aaron Eckhart, \
                    and Abigail Breslin",
                    "Romantic Comedy",
                    "A top chef's life turns upside down \
                    when she suddenly becomes \
                    the guardian of her niece.",
                    "http://ia.media-imdb.com/images/M/MV5BMTI1NzQ5MzU1OV5BMl5BanBnXkFtZTcwNzExODU0MQ@@._V1_SX214_AL_.jpg",   # noqa
                    "https://www.youtube.com/watch?v=APNTQlcbNAI")

# The code below pulls all of the movie info together into
# one list to be used as an argument in the open_movies_page().

movies = [interstellar, good_will_hunt, star_wars,
                  hunger_games, elf, no_reservations]
"""Take arugment of the list to generate the HTML file"""
fresh_tomatoes.open_movies_page(movies)

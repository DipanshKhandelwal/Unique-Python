import media
import my_page


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=LqEszt5wG9I")


ratatouille = media.Movie("Ratatouille",
                     "Storyline",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight In Paris",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
                     "Storyline",
                     "https://upload.wikimedia.org/wikipedia/id/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story , avatar , school_of_rock , ratatouille , midnight_in_paris ,hunger_games]
#my_page.open_movies_page(movies)
print(media.Movie.__doc__)

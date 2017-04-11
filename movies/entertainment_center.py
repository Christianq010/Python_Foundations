import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtube.com")

#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/mk/c/c3/Avatar1.jpg",
                     "https://youtube.com")

#print (avatar.storyline)
#avatar.show_trailer()

thor_ragnorok = media.Movie("Thor: Ragnorok",
                            "This November, Thor: Ragnarok.",
                            "https://upload.wikimedia.org/wikipedia/en/c/cf/Thor-_Ragnarok_logo.jpg",
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU")

#thor_ragnorok.show_trailer()

#save movie objects to array
#movies = [toy_story, avatar, thor_ragnorok]

#fresh_tomatoes.open_movies_page(movies)

#print the predefined variable doc we stored in the class
print (media.Movie.__doc__)
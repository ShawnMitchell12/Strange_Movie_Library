#import the movie data, the classes, and the intro into the main script
from classes import *
from library_data import *
from intro import *

#play the intro
print_intro()


#Creating a function to insert movie genres into the LinkedList
def insert_genre():
    movie_genre_list = LinkedList()
    for movie_genre in genres:
        movie_genre_list.insert_start(movie_genre)
    return movie_genre_list

#Creating function to insert movies into a nested LinkedList of the genre LinkedList
def insert_movie_list():
    movie_data_list = LinkedList()
    for movie_genre in genres:
        movie_sublist = LinkedList()
        for movie in movie_list:
            if movie[0] == movie_genre:
                movie_sublist.insert_start(movie)
        movie_data_list.insert_start(movie_sublist)
    return movie_data_list

#Create lists for user choices
my_genre_list = insert_genre()
my_movie_list = insert_movie_list()

selected_movie_genre = ""

#Create code for User Interaction


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
while len(selected_movie_genre) == 0:
    user_input = str(input(
        "\nWelcome! What genre of strange movie would you like to watch today? Please type in the beginning letter of which genre you choose and press enter.\n")).lower()

    #Search to see if input is in list
    matching_genres = []
    genre_list_head = my_genre_list.get_head_node()
    while genre_list_head is not None:
        if str(genre_list_head.get_value()).startswith(user_input):
            matching_genres.append(genre_list_head.get_value())
        genre_list_head = genre_list_head.get_next_node()

    #Print list of matching genre types
    for movie in matching_genres:
        print(movie)

    #Check case of only one type of movie genre, ask if the user wants this genre
    if len(matching_genres) == 1:
        select_genre = str(input(
            "\nThe only matching genre for the letter you inputted is " + matching_genres[0] + ". \nDo you want to find a movie from the " + matching_genres[0] + " genre? Enter y for yes or n for no\n")).lower()
    
        #After finding which genre, code for pulling relevant movie data
        if select_genre == 'y':
            selected_movie_genre = matching_genres[0]
            print('Selected Movie Genre: ' + selected_movie_genre)
            movie_list_head = my_movie_list.get_head_node()
            while movie_list_head.get_next_node is not None:
                sublist_head = movie_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_movie_genre:
                    while sublist_head.get_next_node() is not None:
                        print("-------------------------------")
                        print('Movie Title: ' + sublist_head.get_value()[1])
                        print('Year Released: ' + sublist_head.get_value()[2])
                        print('Total Runtime: ' + sublist_head.get_value()[3])
                        print('Second Genre Classification: ' + sublist_head.get_value()[4])
                        print('Movie Description: ' + sublist_head.get_value()[5])
                        print('-------------------------------')
                        sublist_head = sublist_head.get_next_node()
                movie_list_head = movie_list_head.get_next_node()

            #Time to ask if the user would like to search for different movies
            repeat_inquiry = str(input('\nWould you like to search for other Strange Movies? Enter y for yes or n for no.\n')).lower()
            if repeat_inquiry == 'y':
                selected_movie_genre = ""

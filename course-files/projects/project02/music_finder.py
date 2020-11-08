from apis import spotify
from apis import sendgrid

def print_menu():
    print('''
---------------------------------------------------------------------
Settings / Browse Options
---------------------------------------------------------------------
1 - Select your favorite genres  
2 - Select your favorite artists 
3 - Discover new music
4 - Quit
---------------------------------------------------------------------
    ''')

def handle_genre_selection():
    print('Handle genre selection here')
    # 1. Allow user to select one or more genres using the 
    #    spotify.get_genres_abridged() function
    # 2. Allow user to store / modify / retrieve genres
    #    in order to get song recommendations 

def handle_artist_selection():
    print('Handle artist selection here...')
    # 1. Allow user to search for an artist using 
    #    spotify.get_artists() function
    # 2. Allow user to store / modify / retrieve artists
    #    in order to get song recommendations

def get_recommendations():
    print('Handle retrieving a list of recommendations here...')
    # 1. Allow user to retrieve song recommendations using the
    #    spotify.get_similar_tracks() function
    # 2. List them below

# Begin Main Program Loop:
while True:
    print_menu()
    choice = input('What would you like to do? ')
    if choice == '1':
        handle_genre_selection()
    elif choice == '2':
        handle_artist_selection()
    elif choice == '3':
        get_recommendations()
        # In addition to showing the user recommendations, allow them
        # to email recommendations to one or more of their friends using
        # the sendgrid.send_mail() function.
    elif choice == '4':
        print('Quitting...')
        break
    else:
        print(choice, 'is an invalid choice. Please try again.')
    print()
    input('Press enter to continue...')

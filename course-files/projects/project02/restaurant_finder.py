from apis import yelp
from apis import sendgrid

def print_menu():
    print('''
---------------------------------------------------------------------
Settings / Browse Options
---------------------------------------------------------------------
1 - Update category filters   
2 - Order by
3 - Browse matching restaurants
4 - Quit
---------------------------------------------------------------------
    ''')

def handle_category_selection():
    print('Handle category selection here')
    # 1. Allow user to select one or more categories using the 
    #    yelp.get_genres_abridged() function
    # 2. Allow user to store / modify / retrieve categories
    #    in order to filter restaurants 

    
def handle_ordering():
    print('Handle ordering preference here...')
    # Allow the user to determine how they want to sort the search results
    # Available options include: best_match, rating, review_count, distance.


def get_matching_restaurants():
    print('Retrieve matching restaurants...')
    # 1. Allow user to retrieve restaurant recommendations using the
    #    yelp.get_businesses() function
    # 2. List them below


# Begin Main Program Loop:
while True:
    print_menu()
    choice = input('What would you like to do? ')
    if choice == '1':
        handle_category_selection()
    elif choice == '2':
        handle_ordering()
    elif choice == '3':
        get_matching_restaurants()
        # In addition to showing the matching restaurants, allow the user to: 
        # (a) select an individual restaurant and view its ratings, and 
        # (b) email a restaurant to one or more of their friends using
        #     the sendgrid.send_mail() function.

    elif choice == '4':
        print('Quitting...')
        break
    else:
        print(choice, 'is an invalid choice. Please try again.')
    print()
    input('Press enter to continue...')

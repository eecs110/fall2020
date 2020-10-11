def get_movie_discount_message(is_senior:bool, is_child:bool, is_student):
    # write a function that returns a message in accordance with the 
    # arguments passed into the functions:
    #  - if they're a senior, tell them they get a discount
    #  - if they're a child, tell them they get a discount
    #  - if they're a student, tell them you need to see their ID
    #  - if they're an adult, tell them that you're going to charge them full price
    pass
    
print(get_movie_discount_message(True, False, False))
print(get_movie_discount_message(False, False, True))
print(get_movie_discount_message(False, False, False))
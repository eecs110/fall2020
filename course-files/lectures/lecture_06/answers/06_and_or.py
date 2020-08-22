def get_movie_discount_message(is_senior:bool, is_child:bool, is_student):
    if is_senior or is_child:
        return '$5 OFF!'
    elif is_student:
        return 'Ask "student" to show ID'
    else:
        return 'Full price!'
    
print(get_movie_discount_message(True, False, False))
print(get_movie_discount_message(False, False, True))
print(get_movie_discount_message(False, False, False))
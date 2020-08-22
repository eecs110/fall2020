# database_functions.py

def _generic_person_characteristic(the_list:list, index:int):
    characteristic_list = []
    for person in the_list:
        characteristic_list.append(person[index])
    return characteristic_list


def get_zip_codes(person_list:list):
    return _generic_person_characteristic(person_list, 4)

def get_names(person_list:list):
    return _generic_person_characteristic(person_list, 0)

def get_occupations(person_list:list):
    return _generic_person_characteristic(person_list, 5)

def filter_by_firefighter(person_list:list):
    firefighters = []
    for person in person_list:
        if 'scientist' in person[5].lower():  # case in-sensitive partial match
            firefighters.append(person)
    return firefighters

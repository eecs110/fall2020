#example: 
eng2sp = {
    'one': 'uno', 
    'two': 'dos', 
    'three': 'tres', 
    'four': 'cuatro', 
    'five': 'cinco', 
    'six': 'seis', 
    'seven': 'siete', 
    'eight': 'ocho', 
    'nine': 'nueve', 
    'ten': 'diez'
}

# things you can do with dictionaries...
print(eng2sp)
print(eng2sp.keys())
print(eng2sp.values())
print(eng2sp['two'])
print(eng2sp.get('three'))
print(eng2sp.get('eleven'))   # use to check to see if an entry exists in the dictionary
# print(eng2sp['eleven'])     # this will throw a KeyError exception



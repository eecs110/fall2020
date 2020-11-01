#example: print all keys and values one by one:
import json
import utilities

# open and read file:
f = open(utilities.get_file_path('eng2sp.json'), 'r')
eng2sp = json.loads(f.read())
f.close()

# Your job:
# Modify the translation program below so that if the translation is not in
# the dictionary, your program will:
# 1. Ask the user to type in the translation so that it can "learn" how to 
#    translate the word.
# 2. Store the new translation in its dictionary,
# 3. When the user asks to quit the program, the program will overwrite
#    the old dictionary with the more comprehensive version of the dictionary
#    (already done for you).

 
while True:
    word = input('Enter a word in English and I will tell you the Spanish translation: ')
    if word.upper() == 'Q':
        print('quitting...\n')
        break
    # YOUR CODE HERE 


    # END YOUR CODE HERE
    print('The translation for', word, 'is', eng2sp.get(word), '\n')


# overwrite eng2sp.json with new dictionary:
f = open(utilities.get_file_path('eng2sp.json'), 'w')
f.write(json.dumps(eng2sp))
f.close()
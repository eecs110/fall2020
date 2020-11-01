#example: print all keys and values one by one:
import json
import utilities

# open and read file:
f = open(utilities.get_file_path('eng2sp.json'), 'r')
eng2sp = json.loads(f.read())
f.close()

# Your job
while True:
    word = input('Enter a word in English and I will tell you the Spanish translation: ')
    if word.upper() == 'Q':
        print('quitting...\n')
        break
    if not eng2sp.get(word):
        translation = input('     Teach me the translation is so that I will remember it for the future: ')
        eng2sp[word] = translation
    print('     The translation for', word, 'is', eng2sp[word], '\n')


# overwrite eng2sp with new dictionary:
f = open(utilities.get_file_path('eng2sp.json'), 'w')
f.write(json.dumps(eng2sp))
f.close()